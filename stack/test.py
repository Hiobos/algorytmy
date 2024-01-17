# test_main.py

import unittest
from main import Stack

class TestStack(unittest.TestCase):

    def test_stack_is_a_class(self):
        self.assertTrue(callable(getattr(Stack, '__init__', None)))

    def test_stack_can_add_and_remove_items(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

    def test_stack_follows_first_in_last_out(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek_returns_first_element_but_doesnt_pop_it(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)

if __name__ == '__main__':
    unittest.main()
