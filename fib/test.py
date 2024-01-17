import unittest
from main import fib

class TestFibonacci(unittest.TestCase):

    def test_fib_function_is_defined(self):
        self.assertTrue(callable(fib))

    def test_calculates_correct_fib_value_for_1(self):
        self.assertEqual(fib(1), 1)

    def test_calculates_correct_fib_value_for_2(self):
        self.assertEqual(fib(2), 1)

    def test_calculates_correct_fib_value_for_3(self):
        self.assertEqual(fib(3), 2)

    def test_calculates_correct_fib_value_for_4(self):
        self.assertEqual(fib(4), 3)

    def test_calculates_correct_fib_value_for_39(self):
        self.assertEqual(fib(39), 63245986)

if __name__ == '__main__':
    unittest.main()