"""
Problem
  
Reverse Words In A Given String
Given a string s, your task is to reverse the words of s.

Example One
{
"s": "best technical interview prep courses",
}
Output:

courses prep interview technical best
Example Two
{
"s": "kickstart",
}
Output:

kickstart
Notes
Constraints:

length of s <= 105
"""

import unittest
import random



def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    return solution(s)

def solution(s):
    words = s.split( )
    words.reverse()
    return " ".join(words)

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reverse_words("best technical interview prep courses"), "courses prep interview technical best")
        self.assertEqual(reverse_words("kickstart"), "kickstart")
        #self.assertEqual(reverse_words(), )



if __name__ == "__main__":
    unittest.main()