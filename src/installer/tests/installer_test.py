import unittest
from unittest.mock import patch
from io import BytesIO
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from installer import Installer
from logger.colors import Colors

class TestInstaller(unittest.TestCase):

    def setUp(self):
        self.cache_path = "/tmp/cache"
        self.installer = Installer(self.cache_path)

    @patch('requests.get')
    def test_install_dep_success(self, mock_get):
        # Mocking the requests.get method
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'fake_binary_content'

        # Testing a successful installation
        result = self.installer.install_dep('https://www.gutenberg.org/files/4484/4484.zip')

        # Assertions
        self.assertTrue(result['result'])
        self.assertEqual(result['errors'], [])
        self.assertIn('Dependency 4484 downloaded from https://www.gutenberg.org/files/4484/4484.zip', result['message'])

    @patch('requests.get')
    def test_install_dep_not_found(self, mock_get):
        # Mocking the requests.get method for a 404 error
        mock_get.return_value.status_code = 404

        # Testing a not found scenario
        result = self.installer.install_dep('http://example.com/nonexistent_dep.zip')

        # Assertions
        self.assertFalse(result['result'])
        self.assertIn('404: File not found.', result['errors'][0])
        self.assertEqual(result['message'], None)

    def test_check_url_consistency_valid_url(self):
        # Testing a valid URL
        url_check_result = self.installer._check_url_consistency('https://www.gutenberg.org/files/4484/4484.zip')

        # Assertions
        self.assertEqual(url_check_result.filename, '4484')
        self.assertEqual(url_check_result.filetype, 'zip')
        self.assertEqual(url_check_result.errors, [])

    def test_check_url_consistency_invalid_url(self):
        # Testing an invalid URL (missing scheme)
        url_check_result = self.installer._check_url_consistency('example.com/invalid_dep.zip')

        # Assertions
        self.assertEqual(url_check_result.filename, 'invalid_dep')
        self.assertEqual(url_check_result.filetype, 'zip')
        self.assertIn(Colors.red("Wrong URL Scheme"), url_check_result.errors)

if __name__ == '__main__':
    unittest.main()
