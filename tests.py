from unittest.mock import patch
import unittest

from shortener import linkInput, checkInput, short

class PasswordsTestCase(unittest.TestCase):

    def linkInput(self):
        user_input = ["www.google.com/"]
        expected_input = "www.google.com/"
        with patch('builtins.input', side_effect=user_input):
            user_in = linkInput()
        self.assertEqual(user_in, expected_input)
    
    def test_checkInput(startLink):
        assert checkInput("www.google.com") == "http://www.google.com"

    def test_short(startLink):
        assert short("www.google.com") == "http://www.bit.ly"[:17]


if __name__ == '__main__':
    unittest.main()
