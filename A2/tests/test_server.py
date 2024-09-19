import unittest
import requests

SERVER_URL = 'http://localhost:5000'

class TestServer(unittest.TestCase):

    def test_send_message(self):
        """Test that a message can be sent successfully."""
        response = requests.post(f'{SERVER_URL}/messages', json={'text': 'Hello, world!'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Message received', response.text)

    def test_message_count(self):
        """Test that the message count is correctly returned."""
        response = requests.get(f'{SERVER_URL}/messages/count')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('count'), int)

    def test_retrieve_messages(self):
        """Test that all messages can be retrieved."""
        response = requests.get(f'{SERVER_URL}/messages')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == '__main__':
    unittest.main()
