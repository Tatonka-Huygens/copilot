import unittest
from unittest.mock import patch
from main import app


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, Jokes!')

    @patch('main.get_joke')
    def test_display_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'Why did the chicken cross the road? To get to the other side.'
        response = self.app.get('/display_joke/Programming?flags=nsfw,religious')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'joke': 'Why did the chicken cross the road? To get to the other side.'})
        mock_get_joke.assert_called_once_with('Programming', 'nsfw,religious')

    @patch('main.search_jokes')
    def test_search_joke(self, mock_search_jokes):
        mock_search_jokes.return_value = 'Why did the chicken go to the seance? To talk to the other side.'
        response = self.app.get('/search_joke/seance')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'joke': 'Why did the chicken go to the seance? To talk to the other side.'})
        mock_search_jokes.assert_called_once_with('seance')


if __name__ == '__main__':
    unittest.main()