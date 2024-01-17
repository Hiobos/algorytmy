most-common-character
Description
This Python project provides a function to find the most commonly used character in a given string.

Usage
main.py
The maxChar function takes a string as input and returns the character that occurs most frequently in the string.

Examples:
python
Copy code
maxChar("abcccccccd")  # Returns: "c"
maxChar("apple 1231111")  # Returns: "1"
Testing
test.py
The test.py file contains unit tests for the maxChar function using the unittest module. The tests cover scenarios such as checking if the function is defined, finding the most frequently used character, and ensuring correct behavior with numbers in the string.

Running Tests
To run the tests, execute test.py in your preferred Python environment.

Example:
bash
Copy code
python test.py