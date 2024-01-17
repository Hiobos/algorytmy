import unittest
from main import capitalize

class TestCapitalize(unittest.TestCase):

    def test_capitalize_is_function(self):
        self.assertTrue(callable(capitalize))

    def test_capitalizes_first_letter_of_every_word(self):
        self.assertEqual(capitalize('hi there, how is it going?'),
                         'Hi There, How Is It Going?')

    def test_capitalizes_first_letter(self):
        self.assertEqual(capitalize('i love breakfast at bill miller bbq'),
                         'I Love Breakfast At Bill Miller Bbq')

if __name__ == '__main__':
    unittest.main()
