"""imports"""
import time
import requests

SERVER_URL = "http://localhost:5000"
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def send_message():
    """Function to send message to server"""
    message = input("Enter your anonymous message: ")
    payload = {"text": message}

    for attempt in range(MAX_RETRIES):
        try:
            print(payload)
            response = requests.post(f"{SERVER_URL}/messages", json=payload, timeout=10)
            print(response.json())
            if response.status_code == 201:
                print("Message sent successfully, ACK received.")
                return True
            print(f"Failed to send message, attempt {attempt + 1}")
            return False
        except requests.ConnectionError: # pragma: no cover
            print(f"Connection error, retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
            return False

    print("Failed to send message after multiple retries.") # pragma: no cover


def get_messages():
    """Function to gett all messages from the server"""
    try:
        response = requests.get(f"{SERVER_URL}/messages", timeout=10)
        if response.status_code == 200:
            messages = response.json()
            print(messages, "------*-*-*-*-*-*-*--*-*-*-*-*-*")
            for msg in messages:
                print(f"[{msg['timestamp']}] {msg['text']}")
            return messages
        print("Failed to retrieve messages.")
        return None
    except requests.ConnectionError: # pragma: no cover
        print("Could not connect to the server.")
        return None


def get_message_count():
    """Function to get number of messages in the server"""
    try:
        response = requests.get(f"{SERVER_URL}/messages/count", timeout=10)
        if response.status_code == 200:
            count = response.json()['count']
            print(f"Total messages: {count}")
            return count
        print("Failed to retrieve message count.")
        return None
    except requests.ConnectionError: # pragma: no cover
        print("Could not connect to the server.")
        return None


if __name__ == '__main__': # pragma: no cover
    while True:
        print("\nOptions:")
        print("1. Send a message")
        print("2. Display all messages")
        print("3. Get message count")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            send_message()
        elif choice == '2':
            get_messages()
        elif choice == '3':
            get_message_count()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
