import requests
import time
import subprocess

server_url = "http://localhost:5000"

def simulate_server_crash():
    print("Simulating server crash...")
    subprocess.run(["pkill", "-f", "server.py"])
    time.sleep(5)
    print("Restarting the server...")
    subprocess.Popen(["python3", "server.py"])
    time.sleep(5)  # Give the server time to restart

def test_recoverability():
    try:
        print("Sending initial message...")
        requests.post(f"{server_url}/messages", json={"text": "Test message before crash"})
        
        print("Simulating server crash and recovery...")
        simulate_server_crash()
        
        print("Verifying if messages were recovered...")
        response = requests.get(f"{server_url}/messages")
        if response.status_code == 200:
            messages = response.json()
            for msg in messages:
                print(f"Recovered message: [{msg['timestamp']}] {msg['text']}")
        else:
            print("Failed to retrieve messages after recovery.")
    except requests.ConnectionError:
        print("Could not connect to the server.")

if __name__ == '__main__':
    test_recoverability()
