"""
Problem
  
First Occurrence Of A Character
Find the first occurrence of a given character in a given string.

Example One
{
"s": "interview",
"to_find": "e"
}
Output:

3
Example Two
{
"s": "kickstart",
"to_find": "n"
}
Output:

-1
Notes
Return -1 if the character is not present.

Constraints:

0 <= length of string <= 104.
Given string contains lower case English alphabets only.
The given character can be any lower case English alphabet.
"""

import unittest
import random


def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    # Write your code here.
    return s.find(to_find)
    

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(find_first_occurrence("kickstart","n"), -1)
        self.assertEqual(find_first_occurrence("interview", "e"), 3)



if __name__ == "__main__":
    unittest.main()