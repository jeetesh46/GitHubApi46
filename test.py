import unittest
from unittest.mock import MagicMock, patch
from github import github_fetch_data

class Github(unittest.TestCase):

    @patch('github.requests.get')
    def test_github_fetch_data_with_mocked_response(self, mock_get):
        # creating a mock response
        mock_response = MagicMock()
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}]'
        mock_get.return_value = mock_response
        mock_get.return_value.status_code = 200
        # calling the function
        response = github_fetch_data('Varun2480')

        # asserting the output
        expected_output = {'repo1': 2, 'repo2': 2}
        self.assertEqual(response, expected_output)

    def test_github_fetch_data_with_real_response(self):
        # calling the function with a real user id
        response = github_fetch_data('Varun2480')

        # asserting that the response is not empty
        self.assertGreater(len(response), 0)

    def test_github_fetch_data_with_invalid_user_id(self):
        # call the function with an invalid user id
        response = github_fetch_data('nonexistentuser')

        # assert that the response is empty
        expected_output = {}
        self.assertEqual(response, expected_output)


if __name__ == '__main__':
    unittest.main()