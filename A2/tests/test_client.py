import unittest
from unittest.mock import patch, MagicMock
import requests
import client  # Assuming client.py contains functions like send_message and check_message_count

class TestClient(unittest.TestCase):

    @patch('builtins.input', side_effect=["Test message"])
    @patch('requests.post')
    def test_send_message_success(self, mock_post, mock_input):
        """Test successful sending of a message."""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response
        
        result = client.send_message()
        mock_input.assert_called_once_with("Enter your anonymous message: ")
        self.assertTrue(result)
        mock_post.assert_called_once_with('http://localhost:5000/messages', json={'text': 'Test message'}, timeout=10)

    @patch('builtins.input', side_effect=["Test message"])
    @patch('requests.post')
    def test_send_message_failure(self, mock_post, mock_input):
        """Test sending a message with failure."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        result = client.send_message()
        self.assertFalse(result)
        mock_input.assert_called_once_with("Enter your anonymous message: ")
        mock_post.assert_called_once_with('http://localhost:5000/messages', json={'text': 'Test message'}, timeout=10)

    @patch('requests.get')
    def test_check_message_count(self, mock_get):
        """Test the client checking the message count."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'count': 5}
        mock_get.return_value = mock_response
        
        count = client.get_message_count()
        self.assertEqual(count, 5)

    @patch('requests.get')
    def test_check_message_count_failure(self, mock_get):
        """Test handling failure in checking message count."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        count = client.get_message_count()
        self.assertIsNone(count)
        mock_get.assert_called_once_with('http://localhost:5000/messages/count', timeout=10)

    @patch('requests.get')
    def test_fetch_messages_success(self, mock_get):
        """Test successfully fetching all messages."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"text": "Hello, world!", "timestamp": "2024-09-19 21:14:26"}, {"text": "Hello, world!", "timestamp": "2024-09-19 21:14:42"}]
        mock_get.return_value = mock_response
        
        messages = client.get_messages()
        self.assertEqual(messages, [{"text": "Hello, world!", "timestamp": "2024-09-19 21:14:26"}, {"text": "Hello, world!", "timestamp": "2024-09-19 21:14:42"}])
        mock_get.assert_called_once_with('http://localhost:5000/messages', timeout=10)

    @patch('requests.get')
    def test_fetch_messages_failure(self, mock_get):
        """Test fetching messages with failure."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        messages = client.get_messages()
        self.assertIsNone(messages)
        mock_get.assert_called_once_with('http://localhost:5000/messages', timeout=10)

    # @patch('builtins.input', side_effect=["Test message"])
    # @patch('client.send_message', return_value=True)
    # def test_interactive_send_message_success(self, mock_send_message, mock_input):
    #     """Test interactive message sending in client."""
    #     client.send_message()
    #     mock_input.assert_called_once_with("Enter your message: ")
    #     mock_send_message.assert_called_once_with("Test message")

    # @patch('builtins.input', side_effect=["Test message"])
    # @patch('client.send_message', return_value=False)
    # def test_interactive_send_message_failure(self, mock_send_message, mock_input):
    #     """Test interactive message sending with failure."""
    #     client.send_message()
    #     mock_input.assert_called_once_with("Enter your message: ")
    #     mock_send_message.assert_called_once_with("Test message")

if __name__ == '__main__':
    unittest.main()
