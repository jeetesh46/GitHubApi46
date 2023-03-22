import unittest
from unittest.mock import MagicMock, patch
from nose.tools import assert_dict_equal, assert_true, assert_false

from github import github_fetch_data

class TestGithub(unittest.TestCase):

    @patch('github.requests.get')
    def test_github_fetch_data_with_mocked_response(self, mock_get):
        # create a mock response
        mock_response = MagicMock()
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]'
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # call the function
        response = github_fetch_data('testing1')

        # assert the output
        expected_output = {'repo1': 3, 'repo2': 3, 'repo3': 3}
        assert_dict_equal(response, expected_output)

    @patch('github.requests.get')
    def test_github_fetch_data_getting_called(self, mock_get):
        # create a mock response
        mock_response = MagicMock()
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]'
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # call the function
        github_fetch_data('test1')

        # assert that requests.get was called
        assert_true(mock_get.called)

    @patch('github.requests.get')
    def test_github_fetch_data_not_getting_called(self, mock_get):
        # call the function with a real user id
        github_fetch_data('jeetesh46')

        # assert that requests.get was not called
        assert_false(mock_get.called)

    @patch('github.requests.get')
    def test_github_fetch_data_with_response_400(self, mock_get):
        # create a mock response with status code 400
        mock_response = MagicMock()
        mock_response.text = '{"error": "status is 400"}'
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        # call the function with a real user id
        response = github_fetch_data('abc')

        # assert that the response is empty
        assert_dict_equal(response, {})

if __name__ == '_main_':
    unittest.main()