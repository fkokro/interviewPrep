"""
Reverse An Array
Reverse a given list of numbers.

Example One
{
"nums": [50, 35, 78, 66, 17]
}
Output:

[17, 66, 78, 35, 50]
Example Two
{
"nums": [50, 40, 30, 20]
}  

Output:

[20, 30, 40, 50]

Notes
Modify the input array in-place and return the modified array.
Constraints:

1 <= size of the input array <= 106
"""

import unittest
import random


def solution(nums):
    return reverse_array(nums)

def reverse_array(nums):
    return nums[::-1]

class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([50, 35, 78, 66, 17]), [17, 66, 78, 35, 50])
        self.assertEqual(solution([50, 40, 30, 20]), [20, 30, 40, 50])
        
        randomList = random.randint(0,100)
    
if __name__ == "__main__":
    unittest.main()