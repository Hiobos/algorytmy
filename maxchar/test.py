# test_main.py

import unittest
from main import maxChar

class TestMaxChar(unittest.TestCase):

    def test_max_char_function_exists(self):
        self.assertTrue(callable(getattr(maxChar, '__call__', None)))

    def test_finds_most_frequently_used_char(self):
        self.assertEqual(maxChar('a'), 'a')
        self.assertEqual(maxChar('abcdefghijklmnaaaaa'), 'a')

    def test_works_with_numbers_in_string(self):
        self.assertEqual(maxChar('ab1c1d1e1f1g1'), '1')

if __name__ == '__main__':
    unittest.main()
