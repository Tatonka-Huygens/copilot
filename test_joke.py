import unittest
from unittest.mock import patch
from joke import get_joke, search_jokes

class JokeTestCase(unittest.TestCase):
    @patch('joke.requests.get')
    def test_get_joke_single(self, mock_get):
        joke_data = {
            'type': 'single',
            'joke': 'Why did the chicken cross the road? To get to the other side.'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = joke_data

        result = get_joke('Programming', 'nsfw,religious')

        self.assertEqual(result, joke_data['joke'])

    @patch('joke.requests.get')
    def test_get_joke_twopart(self, mock_get):
        joke_data = {
            'type': 'twopart',
            'setup': 'Why did the chicken cross the road?',
            'delivery': 'To get to the other side.'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = joke_data

        result = get_joke('Programming', 'nsfw,religious')

        self.assertEqual(result, f"{joke_data['setup']} - {joke_data['delivery']}")

    @patch('joke.requests.get')
    def test_get_joke_no_joke_found(self, mock_get):
        joke_data = {}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = joke_data

        result = get_joke('Programming', 'nsfw,religious')

        self.assertEqual(result, "No joke found.")

    @patch('joke.requests.get')
    def test_search_jokes_found(self, mock_get):
        joke_data = {
            'type': 'single',
            'joke': 'Why did the chicken go to the seance? To talk to the other side.'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = joke_data

        result = search_jokes('seance')

        self.assertEqual(result, joke_data['joke'])

    @patch('joke.requests.get')
    def test_search_jokes_not_found(self, mock_get):
        joke_data = {}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = joke_data

        result = search_jokes('foo')

        self.assertEqual(result, "No joke found.")

if __name__ == '__main__':
    unittest.main()