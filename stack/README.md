stack-data-structure
Description
This Python project provides a simple implementation of a stack data structure.

Usage
stack.py
The Stack class in stack.py represents a stack, allowing you to push, pop, peek, and check if it's empty.

Example Usage:
python
Copy code
from stack import Stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
print(s.pop())  # Output: 1
Testing
test.py
The test.py file contains unit tests for the Stack class using the unittest module. The tests cover scenarios such as checking if the class is defined, adding and removing items, following the Last In, First Out (LIFO) principle, and ensuring peek returns the first element without removing it.

Running Tests
To run the tests, execute test.py in your preferred Python environment.

Example:
bash
Copy code
python test.py