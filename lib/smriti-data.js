export const patient = {
  name: 'Kamala Devi',
  age: 72,
  hometown: 'Kolkata, West Bengal',
  photo: 'https://images.unsplash.com/photo-1660587608077-298c877b2bcd?w=400',
  memoryScore: 78,
  streak: 12,
  favorite_food: 'Aloo posto, rasgulla, and mishti doi',
}

export const family = [
  { id: 'f1', name: 'Amit Sharma', relation: 'Son', location: 'Delhi', photo: 'https://i.pravatar.cc/150?img=12', note: 'Calls every Sunday at 6 PM' },
  { id: 'f2', name: 'Priya Sharma', relation: 'Daughter', location: 'Bangalore', photo: 'https://i.pravatar.cc/150?img=45', note: 'Doctor, video call Wednesdays' },
  { id: 'f3', name: 'Rohan', relation: 'Grandson', location: 'Delhi', photo: 'https://i.pravatar.cc/150?img=8', note: 'Age 8, loves cricket' },
  { id: 'f4', name: 'Neha', relation: 'Granddaughter', location: 'Bangalore', photo: 'https://i.pravatar.cc/150?img=47', note: 'Age 5, loves drawing' },
  { id: 'f5', name: 'Rakesh (Late)', relation: 'Husband', location: 'Memory', photo: 'https://i.pravatar.cc/150?img=60', note: 'Married in 1975, retired teacher' },
]

export const schedule = [
  { time: '07:30', title: 'Morning tea & pranayama', icon: 'sun', done: true },
  { time: '10:00', title: 'Blood pressure medicine (Amlodipine 5mg)', icon: 'pill', done: true },
  { time: '13:00', title: 'Lunch with caregiver Meera', icon: 'utensils', done: false },
  { time: '17:00', title: 'Video call with Priya', icon: 'video', done: false },
  { time: '20:00', title: 'Memory medicine (Donepezil 10mg)', icon: 'pill', done: false },
]

export const medicines = [
  { id: 'm1', name: 'Amlodipine', dose: '5 mg', time: '10:00 AM', purpose: 'Blood pressure', status: 'taken', color: 'from-sky-400 to-blue-500' },
  { id: 'm2', name: 'Metformin', dose: '500 mg', time: '01:00 PM', purpose: 'Diabetes', status: 'upcoming', color: 'from-teal-400 to-emerald-500' },
  { id: 'm3', name: 'Donepezil', dose: '10 mg', time: '08:00 PM', purpose: 'Memory support', status: 'upcoming', color: 'from-violet-400 to-purple-500' },
  { id: 'm4', name: 'Vitamin D3', dose: '1 tab', time: '09:00 AM', purpose: 'Bone health', status: 'missed', color: 'from-amber-400 to-orange-500' },
]

export const timeline = [
  { id: 't1', year: 1975, title: 'Wedding Day', desc: 'Married Rakesh in Kolkata surrounded by loved ones', people: ['Rakesh', 'Parents'], location: 'Kolkata', img: 'https://images.unsplash.com/photo-1583072535333-7395fd58d495?w=800' },
  { id: 't2', year: 1980, title: 'Amit was born', desc: 'Our beautiful son Amit came into our lives', people: ['Amit'], location: 'Kolkata', img: 'https://images.unsplash.com/photo-1503516459261-40c66117780a?w=800' },
  { id: 't3', year: 1998, title: 'Priya\'s Graduation', desc: 'Daughter graduated as a doctor from AIIMS', people: ['Priya'], location: 'Delhi', img: 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800' },
  { id: 't4', year: 2016, title: 'Rohan\'s Birth', desc: 'First grandchild Rohan was born', people: ['Rohan', 'Amit'], location: 'Delhi', img: 'https://images.unsplash.com/photo-1519689680058-324335c77eba?w=800' },
  { id: 't5', year: 2023, title: 'Durga Puja in Kolkata', desc: 'Whole family celebrated together at home', people: ['Amit', 'Priya', 'Grandchildren'], location: 'Kolkata', img: 'https://images.unsplash.com/photo-1601987077677-5346c0c57d3f?w=800' },
  { id: 't6', year: 2024, title: 'Family Trip to Shillong', desc: 'A wonderful vacation with the whole family', people: ['Family'], location: 'Shillong', img: 'https://images.unsplash.com/photo-1514415008039-efa173293080?w=800' },
  { id: 't7', year: 2025, title: 'Neha\'s 5th Birthday', desc: 'Celebrated with cake and lots of drawings', people: ['Neha', 'Priya'], location: 'Bangalore', img: 'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800' },
]

export const memoryBank = {
  family,
  places: [ { id: 'p1', name: 'Howrah Bridge', desc: 'Loved evening walks here' }, { id: 'p2', name: 'Victoria Memorial', desc: 'Anniversary photos' }, { id: 'p3', name: 'Shillong', desc: '2024 family trip' } ],
  foods: [ { id: 'fd1', name: 'Aloo Posto', desc: 'Home comfort' }, { id: 'fd2', name: 'Rasgulla', desc: 'Weekly treat' }, { id: 'fd3', name: 'Mishti Doi', desc: 'Sweet yogurt' } ],
  dates: [ { id: 'd1', name: 'Anniversary', date: 'Nov 12' }, { id: 'd2', name: 'Amit\'s Birthday', date: 'Mar 3' }, { id: 'd3', name: 'Priya\'s Birthday', date: 'Jul 21' } ],
  notes: [ { id: 'n1', name: 'Allergy', desc: 'Allergic to sulfa drugs' }, { id: 'n2', name: 'Doctor', desc: 'Dr. Banerjee, Apollo Kolkata' } ],
}

export const games = [
  { id: 'g1', name: 'Who Is This?', desc: 'Identify family members from photos', difficulty: 'Easy', score: 85, accuracy: 92, played: 24, badge: 'Gold', color: 'from-sky-500 to-blue-600', emoji: '👥' },
  { id: 'g2', name: 'Memory Match', desc: 'Match pairs of memory cards', difficulty: 'Medium', score: 72, accuracy: 78, played: 18, badge: 'Silver', color: 'from-violet-500 to-purple-600', emoji: '🃏' },
  { id: 'g3', name: 'Remember Sequence', desc: 'Repeat the color/sound pattern', difficulty: 'Medium', score: 68, accuracy: 74, played: 15, badge: 'Silver', color: 'from-teal-500 to-emerald-600', emoji: '🔢' },
  { id: 'g4', name: 'Family Relationship Quiz', desc: 'How is this person related?', difficulty: 'Easy', score: 90, accuracy: 95, played: 30, badge: 'Gold', color: 'from-pink-500 to-rose-600', emoji: '👪' },
  { id: 'g5', name: 'Event Recall Challenge', desc: 'Recall details of past events', difficulty: 'Hard', score: 61, accuracy: 66, played: 9, badge: 'Bronze', color: 'from-amber-500 to-orange-600', emoji: '🎞️' },
]

export const progressData = {
  weekly: [ { day: 'Mon', memory: 65, activity: 40 }, { day: 'Tue', memory: 70, activity: 55 }, { day: 'Wed', memory: 68, activity: 60 }, { day: 'Thu', memory: 74, activity: 65 }, { day: 'Fri', memory: 78, activity: 70 }, { day: 'Sat', memory: 80, activity: 75 }, { day: 'Sun', memory: 82, activity: 80 } ],
  gameAccuracy: [ { name: 'Who Is This?', value: 92 }, { name: 'Memory Match', value: 78 }, { name: 'Sequence', value: 74 }, { name: 'Family Quiz', value: 95 }, { name: 'Event Recall', value: 66 } ],
  reminderCompletion: [ { day: 'Mon', completed: 4, missed: 1 }, { day: 'Tue', completed: 5, missed: 0 }, { day: 'Wed', completed: 5, missed: 0 }, { day: 'Thu', completed: 4, missed: 1 }, { day: 'Fri', completed: 5, missed: 0 }, { day: 'Sat', completed: 3, missed: 2 }, { day: 'Sun', completed: 5, missed: 0 } ],
  monthly: [ { m: 'Jan', v: 58 }, { m: 'Feb', v: 62 }, { m: 'Mar', v: 65 }, { m: 'Apr', v: 68 }, { m: 'May', v: 72 }, { m: 'Jun', v: 78 } ],
}

export const emergencyContacts = [
  { id: 'e1', name: 'Amit (Son)', phone: '+91 98100 12345', primary: true },
  { id: 'e2', name: 'Priya (Daughter)', phone: '+91 98800 67890', primary: false },
  { id: 'e3', name: 'Dr. Banerjee', phone: '+91 98300 55555', primary: false },
  { id: 'e4', name: 'Meera (Caregiver)', phone: '+91 98310 11223', primary: false },
]

export const initialChat = [
  { role: 'assistant', content: 'Namaste Kamala ji 💙 I am SmritiSaathi, your memory companion. How are you feeling today?' },
]
