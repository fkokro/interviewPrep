"""
Problem
  
Convert Uppercase Characters To Lowercase
Convert all uppercase characters to lowercase in a given string.

Example One
{
"s": "InTerView"
}
Output:

"interview"
Example Two
{
"s": "KICKSTART"
}
Output:

"kickstart"
Notes
Constraints:

0 <= length of string <= 104
Given string contains uppercase and lowercase English alphabets only.
"""

import unittest
import random


def uppercase_to_lowercase(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    return s.lower()

def solution(s):
    pass

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(uppercase_to_lowercase("InTerView"), "interview")
        self.assertEqual(uppercase_to_lowercase("KICKSTART"), "kickstart")


if __name__ == "__main__":
    unittest.main()