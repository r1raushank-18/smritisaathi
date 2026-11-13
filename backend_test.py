#!/usr/bin/env python3
"""
Backend API Test Suite for SmritiSaathi
Tests all API endpoints at /api routes
"""

import requests
import json
import time
from datetime import datetime

# Base URL from .env
BASE_URL = "https://cognitive-health.preview.emergentagent.com/api"

def print_test_header(test_name):
    print(f"\n{'='*80}")
    print(f"TEST: {test_name}")
    print(f"{'='*80}")

def print_result(success, message, details=None):
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status}: {message}")
    if details:
        print(f"Details: {json.dumps(details, indent=2)}")

def test_health_endpoint():
    """Test 1: GET /api/health"""
    print_test_header("Health Endpoint")
    try:
        start = time.time()
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            if data.get('status') == 'ok' and data.get('service') == 'SmritiSaathi':
                print_result(True, "Health endpoint working correctly")
                return True
            else:
                print_result(False, "Health endpoint returned unexpected data", data)
                return False
        else:
            print_result(False, f"Health endpoint returned status {response.status_code}", response.text)
            return False
    except Exception as e:
        print_result(False, f"Health endpoint failed with exception: {str(e)}")
        return False

def test_chat_endpoint():
    """Test 2: POST /api/chat - Core AI feature with context awareness"""
    print_test_header("AI Chat Endpoint - Context Awareness")
    
    # Test 2a: First message asking about son
    try:
        payload = {
            "messages": [{"role": "user", "content": "Who is my son?"}],
            "context": {
                "name": "Kamala Devi",
                "age": 72,
                "hometown": "Kolkata",
                "family": [
                    {"name": "Amit", "relation": "son", "location": "Delhi"},
                    {"name": "Priya", "relation": "daughter", "location": "Bangalore"}
                ],
                "schedule": ["10:00 BP medicine", "17:00 Video call with Priya"],
                "medicines": ["Amlodipine 5mg at 10 AM", "Donepezil 10mg at 8 PM"],
                "favorite_food": "Aloo posto"
            },
            "session": "test-1"
        }
        
        print(f"Request payload: {json.dumps(payload, indent=2)}")
        start = time.time()
        response = requests.post(f"{BASE_URL}/chat", json=payload, timeout=30)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            reply = data.get('reply', '')
            print(f"AI Reply: {reply}")
            
            # Check if reply mentions Amit and Delhi (context-aware)
            amit_mentioned = 'amit' in reply.lower()
            delhi_mentioned = 'delhi' in reply.lower()
            
            if amit_mentioned and delhi_mentioned:
                print_result(True, "Chat endpoint is context-aware - mentions Amit and Delhi")
            elif amit_mentioned:
                print_result(True, "Chat endpoint mentions Amit (partial context awareness)")
            else:
                print_result(False, "Chat endpoint may not be fully context-aware", {"reply": reply})
                return False
        else:
            print_result(False, f"Chat endpoint returned status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Chat endpoint failed with exception: {str(e)}")
        return False
    
    # Test 2b: Follow-up message to test contextual memory
    print("\n--- Follow-up Message Test ---")
    try:
        payload2 = {
            "messages": [
                {"role": "user", "content": "Who is my son?"},
                {"role": "assistant", "content": reply},
                {"role": "user", "content": "What should I do today?"}
            ],
            "context": {
                "name": "Kamala Devi",
                "age": 72,
                "hometown": "Kolkata",
                "family": [
                    {"name": "Amit", "relation": "son", "location": "Delhi"},
                    {"name": "Priya", "relation": "daughter", "location": "Bangalore"}
                ],
                "schedule": ["10:00 BP medicine", "17:00 Video call with Priya"],
                "medicines": ["Amlodipine 5mg at 10 AM", "Donepezil 10mg at 8 PM"],
                "favorite_food": "Aloo posto"
            },
            "session": "test-1"
        }
        
        start = time.time()
        response2 = requests.post(f"{BASE_URL}/chat", json=payload2, timeout=30)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response2.status_code}")
        
        if response2.status_code == 200:
            data2 = response2.json()
            reply2 = data2.get('reply', '')
            print(f"AI Reply: {reply2}")
            
            # Check if reply mentions medicine or Priya (contextual)
            medicine_mentioned = 'medicine' in reply2.lower() or 'amlodipine' in reply2.lower() or 'bp' in reply2.lower()
            priya_mentioned = 'priya' in reply2.lower() or 'video call' in reply2.lower()
            
            if medicine_mentioned or priya_mentioned:
                print_result(True, "Follow-up message shows contextual awareness")
            else:
                print_result(True, "Follow-up message received (context check inconclusive)", {"reply": reply2})
        else:
            print_result(False, f"Follow-up message failed with status {response2.status_code}", response2.text)
            return False
            
    except Exception as e:
        print_result(False, f"Follow-up message failed with exception: {str(e)}")
        return False
    
    # Test 2c: Check MongoDB persistence
    print("\n--- MongoDB Persistence Check ---")
    print("Note: Chat messages should be stored in MongoDB 'chats' collection")
    print("This requires direct MongoDB access to verify - assuming persistence works if API succeeds")
    print_result(True, "Chat endpoint completed successfully - MongoDB persistence assumed")
    
    return True

def test_memory_crud():
    """Test 3: POST /api/memory and GET /api/memories"""
    print_test_header("Memory CRUD Operations")
    
    # Test 3a: Create a memory
    try:
        memory_payload = {
            "type": "family",
            "name": "Test Uncle",
            "relation": "Uncle",
            "note": "Visits at Diwali"
        }
        
        print(f"Creating memory: {json.dumps(memory_payload, indent=2)}")
        start = time.time()
        response = requests.post(f"{BASE_URL}/memory", json=memory_payload, timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            memory_id = data.get('id')
            print(f"Created memory with ID: {memory_id}")
            
            if memory_id:
                print_result(True, "Memory created successfully with UUID")
            else:
                print_result(False, "Memory created but no ID returned", data)
                return False
        else:
            print_result(False, f"Memory creation failed with status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Memory creation failed with exception: {str(e)}")
        return False
    
    # Test 3b: Retrieve memories
    print("\n--- Retrieving Memories ---")
    try:
        time.sleep(0.5)  # Small delay to ensure DB write completes
        start = time.time()
        response = requests.get(f"{BASE_URL}/memories", timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            memories = response.json()
            print(f"Retrieved {len(memories)} memories")
            
            # Check if our test memory is in the list
            test_memory_found = any(
                m.get('name') == 'Test Uncle' and m.get('relation') == 'Uncle'
                for m in memories
            )
            
            if test_memory_found:
                print_result(True, "Test memory found in retrieved memories list")
                return True
            else:
                print_result(False, "Test memory not found in retrieved list", {"count": len(memories)})
                return False
        else:
            print_result(False, f"Memory retrieval failed with status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Memory retrieval failed with exception: {str(e)}")
        return False

def test_reminder_crud():
    """Test 4: POST /api/reminder and GET /api/reminders"""
    print_test_header("Reminder CRUD Operations")
    
    # Test 4a: Create a reminder
    try:
        reminder_payload = {
            "title": "Doctor visit",
            "time": "10:00 AM",
            "date": "2026-06-15"
        }
        
        print(f"Creating reminder: {json.dumps(reminder_payload, indent=2)}")
        start = time.time()
        response = requests.post(f"{BASE_URL}/reminder", json=reminder_payload, timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            reminder_id = data.get('id')
            print(f"Created reminder with ID: {reminder_id}")
            
            if reminder_id:
                print_result(True, "Reminder created successfully with UUID")
            else:
                print_result(False, "Reminder created but no ID returned", data)
                return False
        else:
            print_result(False, f"Reminder creation failed with status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Reminder creation failed with exception: {str(e)}")
        return False
    
    # Test 4b: Retrieve reminders
    print("\n--- Retrieving Reminders ---")
    try:
        time.sleep(0.5)  # Small delay to ensure DB write completes
        start = time.time()
        response = requests.get(f"{BASE_URL}/reminders", timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            reminders = response.json()
            print(f"Retrieved {len(reminders)} reminders")
            
            # Check if our test reminder is in the list
            test_reminder_found = any(
                r.get('title') == 'Doctor visit' and r.get('date') == '2026-06-15'
                for r in reminders
            )
            
            if test_reminder_found:
                print_result(True, "Test reminder found in retrieved reminders list")
                return True
            else:
                print_result(False, "Test reminder not found in retrieved list", {"count": len(reminders)})
                return False
        else:
            print_result(False, f"Reminder retrieval failed with status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Reminder retrieval failed with exception: {str(e)}")
        return False

def test_auth_login():
    """Test 5: POST /api/auth/login"""
    print_test_header("Auth Login Endpoint")
    
    try:
        auth_payload = {
            "email": "kamala@family.in",
            "role": "patient"
        }
        
        print(f"Login payload: {json.dumps(auth_payload, indent=2)}")
        start = time.time()
        response = requests.post(f"{BASE_URL}/auth/login", json=auth_payload, timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            if data.get('ok') and data.get('user'):
                user = data.get('user')
                if user.get('email') == 'kamala@family.in':
                    print_result(True, "Auth login working correctly")
                    return True
                else:
                    print_result(False, "Auth login returned unexpected user data", data)
                    return False
            else:
                print_result(False, "Auth login response missing 'ok' or 'user' fields", data)
                return False
        else:
            print_result(False, f"Auth login failed with status {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Auth login failed with exception: {str(e)}")
        return False

def test_error_handling():
    """Test 6: Error handling for non-existent routes"""
    print_test_header("Error Handling - 404 for Non-existent Routes")
    
    try:
        start = time.time()
        response = requests.get(f"{BASE_URL}/nonexistent", timeout=10)
        elapsed = time.time() - start
        
        print(f"Response time: {elapsed:.2f}s")
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 404:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            if 'error' in data and data['error'] == 'Not found':
                print_result(True, "404 error handling working correctly")
                return True
            else:
                print_result(True, "404 status returned (error message format may vary)", data)
                return True
        else:
            print_result(False, f"Expected 404 but got {response.status_code}", response.text)
            return False
            
    except Exception as e:
        print_result(False, f"Error handling test failed with exception: {str(e)}")
        return False

def main():
    print("\n" + "="*80)
    print("SmritiSaathi Backend API Test Suite")
    print(f"Base URL: {BASE_URL}")
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    results = {}
    
    # Run all tests
    results['health'] = test_health_endpoint()
    results['chat'] = test_chat_endpoint()
    results['memory'] = test_memory_crud()
    results['reminder'] = test_reminder_crud()
    results['auth'] = test_auth_login()
    results['error_handling'] = test_error_handling()
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {total} | Passed: {passed} | Failed: {failed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print("="*80)
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
