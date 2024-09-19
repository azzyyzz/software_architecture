"""imports"""
from datetime import datetime
import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# File to persist messages
MESSAGE_FILE = 'messages.json'

# Load messages from file if it exists
if os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, 'r', encoding='UTF-8') as file:
        messages = json.load(file)
else:
    messages = []


def save_messages():
    """Function to save messages to file"""
    with open(MESSAGE_FILE, 'w', encoding='UTF-8') as messages_file:
        json.dump(messages, messages_file)


@app.route('/messages', methods=['POST'])
def send_message():
    """Endpoint to send a message with acknowledgment"""
    data = request.json
    message = {
        'text': data['text'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    messages.append(message)
    save_messages()  # Persist messages to file after adding a new one
    return jsonify({'status': 'Message received successfully'}), 201  # ACK


@app.route('/messages', methods=['GET'])
def get_messages():
    """Endpoint to retrieve all messages"""
    return jsonify(messages), 200


@app.route('/messages/count', methods=['GET'])
def message_count():
    """Endpoint to get the count of messages"""
    return jsonify({'count': len(messages)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
