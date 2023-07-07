import unittest
from unittest.mock import patch
from unittest.mock import mock_open
from openai_chat import OpenAIChat 

class TestOpenAIChat(unittest.TestCase):
    def setUp(self):
        self.chat = OpenAIChat(instructions="You are a helpful assistant.")

    def test_make_gpt3_request(self):
        with patch('openai.ChatCompletion.create') as mock_create:
            mock_create.return_value = {
                'choices': [{'message': {'content': 'Hello!'}}]
            }
            response = self.chat.make_gpt3_request('Hi there!')

            # Asserting the type and content of the response
            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 3)
            self.assertEqual(response[0]['role'], 'system')
            self.assertEqual(response[0]['content'], self.chat.instructions)
            self.assertEqual(response[1]['role'], 'user')
            self.assertEqual(response[1]['content'], 'Hi there!')
            self.assertEqual(response[2]['role'], 'assistant')
            self.assertEqual(response[2]['content'], 'Hello!')

    def test_clear_history(self):
        self.chat.history = [{'role': 'user', 'content': 'Hello!'}]
        self.chat.clear_history()
        self.assertEqual(self.chat.history, [])

    def test_parse_history(self):
        self.chat.history = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'Hi there!'},
            {'role': 'assistant', 'content': 'Hello!'}
        ]
        messages = self.chat.parse_history(self.chat.history)
        self.assertEqual(len(messages), 3)
        self.assertEqual(messages[0], 'System: You are a helpful assistant.')
        self.assertEqual(messages[1], 'You: Hi there!')
        self.assertEqual(messages[2], 'Assistant: Hello!')

    @patch('openai.ChatCompletion.create')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_history(self, mock_open, mock_create):
        # Mocking the openai.ChatCompletion.create response
        mock_create.return_value = {
            'choices': [{'message': {'content': 'conversation1'}}]
        }
        self.chat.make_gpt3_request('Hi there!')
        self.chat.save_history()
        mock_open.assert_called_once_with('history/conversation1.json', 'w')

    @patch('os.listdir')
    def test_get_history_files(self, mock_listdir):
        # Mocking the os.listdir response
        mock_listdir.return_value = ['history1.json', 'history2.json']
        files = self.chat.get_history_files()
        self.assertEqual(files, ['history1.json', 'history2.json'])

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_history(self, mock_json_load, mock_open):
        # Mocking the json.load response
        mock_json_load.return_value = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'Hello!'},
            {'role': 'assistant', 'content': 'Hi there!'}
        ]
        self.chat.load_history('history1.json')
        mock_open.assert_called_once_with('history/history1.json')
        self.assertEqual(len(self.chat.history), 3)

if __name__ == '__main__':
    unittest.main()