import unittest
from unittest import mock

from gitignore_parser import parse_gitignore


class Test(unittest.TestCase):

    def test_parse_gitignore(self):

        data = '''/vendor/
/stuff/ 
'''
        mock_open = mock.mock_open(read_data=data)
        with mock.patch('builtins.open', mock_open):
            match = parse_gitignore('/path/to/.gitignore')
            self.assertTrue(match('/vendor'))


