"""
Problem
  
Find Pivot Index
Given a list of integers numbers, calculate the pivot index of this list.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example One
{
"numbers": [2, 3, 1, -1, 1, 1, 4]
}
Output:

2
Considering index 2 as pivot index, left subarray = [2, 3] and right subarray = [-1, 1, 1, 4]. Here, sum(left subarray) = sum(right subarray) = 5.

Here, index 4 is also a valid pivot index. But index 2 is leftmost.

Example Two
{
"numbers": [2, 3, 5]
}
Output:

-1
Example Three
{
"numbers": [0, 1, -1]
}
Output:

0
Notes
Constraints:

1 <= size of the input list <= 104
-105 <= any element of the input list <= 105
"""

import unittest
import random



def get_pivot_index(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    return solution(numbers)

def solution(numbers):
    total = sum(numbers)
    left_sum = 0

    for idx, val in enumerate(numbers):
        right_sum = total - left_sum - val
        if right_sum == left_sum:
            return (idx)
        left_sum += val

    return - 1


class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(get_pivot_index([2, 3, 1, -1, 1, 1, 4]), 2)
        self.assertEqual(get_pivot_index([2, 3, 5]), -1)
        self.assertEqual(get_pivot_index([0, 1, -1]), 0)



if __name__ == "__main__":
    unittest.main()