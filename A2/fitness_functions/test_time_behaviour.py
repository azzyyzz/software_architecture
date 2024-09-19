import time
import requests

SERVER_URL = 'http://localhost:5000'

def measure_time_behavior():
    """Measure response time for sending a message and checking message count."""
    
    start_time = time.time()
    
    # Send a message
    message_response = requests.post(f'{SERVER_URL}/messages', json={'text': 'Test message'})
    send_time = time.time() - start_time
    
    if message_response.status_code == 201:
        print(f"Message sent in {send_time:.4f} seconds")
    else:
        print("Failed to send message.")
    
    # Check message count
    start_time = time.time()
    count_response = requests.get(f'{SERVER_URL}/messages/count')
    count_time = time.time() - start_time
    
    if count_response.status_code == 200:
        print(f"Message count retrieved in {count_time:.4f} seconds")
    else:
        print("Failed to retrieve message count.")
    
if __name__ == "__main__":
    measure_time_behavior()
