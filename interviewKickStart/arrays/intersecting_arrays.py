"""
Problem
  
Intersection Of Two Arrays
Given two lists of numbers, find their intersection.

Example One
{
"a": [4, 2, 2, 3, 1],
"b": [2, 2, 2, 3, 3]
}
Output:

[2, 2, 3]
Example Two
{
"a": [6, 2, 4],
"b": [1, 5, 3, 7]
}
Output:

[]
Notes
The order of elements in the output list does not matter.
The frequency of any number in the intersection must be equal to the minimum of the frequency of that number in both the given lists.
Constraints:

1 <= size of the input lists <= 105
-106 <= any element of the input lists <= 106
"""

import unittest
import random


def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return solution(a, b)
    
def solution(a, b):
    from collections import Counter
    #hashmaps
    freq_a = Counter(a)
    freq_b = Counter(b)

    result = []

    for num in freq_a:
        if num in freq_b:
            result.extend([num] * min(freq_a[num], freq_b[num]))

    return result

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(get_intersection_with_maintained_frequency([4, 2, 2, 3, 1], [2, 2, 2, 3, 3]), [2, 2, 3])
        self.assertEqual(get_intersection_with_maintained_frequency([6, 2, 4], [1, 5, 3, 7]), [])



if __name__ == "__main__":
    unittest.main()