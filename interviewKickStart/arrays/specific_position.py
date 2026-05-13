"""
Problem
  
Insert An Element At A Specific Position In An Array
Given an array of numbers, insert a given element at the specified position in the array.

Example One
{
"nums": [2, 4, 5, 6, -1],
"element": 3,
"position": 2
}
Output:

[2, 3, 4, 5, 6]
Example Two
{
"nums": [70, 60, 50, -1],
"element": 40,
"position": 4
}
Output:

[70, 60, 50, 40]
Notes
The last element of the array is -1 indicating a blank position.
The given position follows 1-based indexing.
Return the modified array.
Constraints:

2 <= size of the input array <= 106
0 <= elements of the array <= 106
1 <= position <= size of the input array
"""

import unittest
import random


def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return solution(nums, element, position)

def solution(nums, element, position):
    nums.insert(position - 1, element)
    nums.pop(-1)
    return nums

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(insert_element_at_position([2, 4, 5, 6, -1], 3, 2), [2, 3, 4, 5, 6])
        self.assertEqual(insert_element_at_position([70, 60, 50, -1], 40, 4), [70, 60, 50, 40])



if __name__ == "__main__":
    unittest.main()