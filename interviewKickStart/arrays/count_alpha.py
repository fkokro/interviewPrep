
"""
Problem
  
Count Alphabets
Count the number of alphabets in a given string.

Example One
{
"s": "#aBdj12C"
}
Output:

5
Example Two
{
"s": "123 !@#$"
}
Output:

0
Notes
Constraints:

0 <= length of string <= 104
String contains lower case and upper case English alphabets, digits, and some special characters('!', '@', '#', '$', '*', ' ') only.
"""
import random
import unittest


def count_alphabets(s):
    """
    Args:
    s(str)
    Returns:
     int32
    """
    # Write your code here.
    return solution(s)

def solution(s):
    count = 0
    for ch in s:
        if ch.isalpha():
            count += 1
    return count

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_alphabets("#aBdj12C"), 5)
        self.assertEqual(count_alphabets("123 !@#$"), 0)


if __name__ == "__main__":
    unittest.main()