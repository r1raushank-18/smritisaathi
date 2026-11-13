'use client'

// Central "natural voice" helper.
// Primary: OpenAI TTS (via /api/tts) — warm human-like voice (nova/shimmer/alloy).
// Fallback: browser SpeechSynthesis if the network is unavailable.

let currentAudio = null
let currentUrl = null
let speaking = false
const cache = new Map() // text::voice -> objectUrl

function stripEmoji(text) {
  return (text || '').replace(/[\p{Extended_Pictographic}\uFE0F]/gu, '').replace(/\s+/g, ' ').trim()
}

// Voice options tuned for warmth & clarity for elderly listeners
export const VOICE_CHOICES = {
  'en-IN': 'nova',    // warm female
  'hi-IN': 'shimmer', // soft female
  'bn-IN': 'shimmer',
  default: 'nova',
}

export function stopSpeaking() {
  if (currentAudio) { try { currentAudio.pause(); currentAudio.currentTime = 0 } catch (e) {} }
  if (typeof window !== 'undefined' && window.speechSynthesis) window.speechSynthesis.cancel()
  speaking = false
}

export function isSpeaking() { return speaking }

export async function speak(text, opts = {}) {
  const clean = stripEmoji(text)
  if (!clean) return
  const lang = opts.lang || 'en-IN'
  const voice = opts.voice || VOICE_CHOICES[lang] || VOICE_CHOICES.default
  const speed = opts.speed || 0.95
  const onEnd = opts.onEnd

  stopSpeaking()

  // Try premium TTS
  try {
    const cacheKey = `${voice}::${clean}`
    let url = cache.get(cacheKey)
    if (!url) {
      const res = await fetch('/api/tts', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text: clean, voice, speed }) })
      if (!res.ok) throw new Error('TTS failed')
      const blob = await res.blob()
      url = URL.createObjectURL(blob)
      cache.set(cacheKey, url)
      // Bound cache size
      if (cache.size > 30) { const first = cache.keys().next().value; URL.revokeObjectURL(cache.get(first)); cache.delete(first) }
    }
    const audio = new Audio(url)
    audio.playbackRate = 1
    audio.volume = 1
    currentAudio = audio; currentUrl = url; speaking = true
    audio.onended = () => { speaking = false; currentAudio = null; onEnd?.() }
    audio.onerror = () => { speaking = false; currentAudio = null; fallback() }
    await audio.play()
    return
  } catch (e) {
    // Fallback to browser
  }

  function fallback() {
    if (typeof window === 'undefined' || !window.speechSynthesis) return
    const u = new SpeechSynthesisUtterance(clean)
    const voices = window.speechSynthesis.getVoices()
    const rules = [
      v => new RegExp(`^${lang}$`, 'i').test(v.lang) && /female|natural|neural|online|priya|kalpana|aditi/i.test(v.name),
      v => new RegExp(`^${lang.split('-')[0]}`, 'i').test(v.lang) && /google|microsoft|natural/i.test(v.name),
      v => new RegExp(`^${lang}$`, 'i').test(v.lang),
      v => /en-IN|en-GB/i.test(v.lang),
    ]
    let chosen = null
    for (const r of rules) { chosen = voices.find(r); if (chosen) break }
    if (chosen) { u.voice = chosen; u.lang = chosen.lang } else u.lang = lang
    u.rate = 0.95; u.pitch = 1.05
    u.onend = () => { speaking = false; onEnd?.() }
    speaking = true
    window.speechSynthesis.speak(u)
  }
  fallback()
}
