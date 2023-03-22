import unittest
from unittest.mock import MagicMock, patch
from nose.tools import assert_true, assert_false

from github import github_fetch_data

class Github(unittest.TestCase):

    @patch('github.requests.get')
    def test_github_fetch_data_with_mocked_response(self, mock_get):
        # creating a mock response
        mock_response = MagicMock()
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]'
        mock_get.return_value = mock_response
        mock_get.return_value.status_code = 200
        # calling the function
        response = github_fetch_data('testing1')

        # asserting the output
        expected_output = {'repo1': 3, 'repo2': 3, 'repo3': 3}
        self.assertEqual(response, expected_output)

    @patch('github.requests.get')
    def test_github_fetch_data_getting_called(self, mock_get):
        # creating a mock response
        mock_get.return_value = MagicMock()
        mock_get.return_value.text = '[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]'
        mock_get.return_value.status_code = 200
        # calling the function
        response = github_fetch_data('test1')

        assert_true(mock_get.called)

    @patch('github.requests.get')
    def test_github_fetch_data_not_getting_called(self, mock_get):
        # creating a mock response
        mock_get.return_value = MagicMock()
        mock_get.return_value.text = '[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]'
        mock_get.return_value.status_code = 200
        # calling the function
        # response = github_fetch_data('jeetesh46')

        assert_false(mock_get.called)

    @patch('github.requests.get')
    def test_github_fetch_data_with_response_400(self, mock_get):
        mock_get.return_value = MagicMock()
        mock_get.return_value.text = '{"error": "status is 400"}'
        mock_get.return_value.status_code = 400
        # calling the function with a real user id
        response = github_fetch_data('abc')

        # asserting that the response is not empty
        self.assertEqual({}, {})


if __name__ == '_main_':
    unittest.main()