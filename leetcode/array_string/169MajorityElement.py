"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
import unittest


def majorityElement(nums: list[int]) -> int:
        freq = {}
        maxOccurance = 0
        maxKey = 0

        for ele in nums:
            if ele in freq.keys():
                freq[ele] += 1
            else:
                freq[ele] = 1
                
        for key, ele in freq.items():
            if ele > maxOccurance:
                maxKey = key
                maxOccurance = ele
                
        return maxKey

class testSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(majorityElement([3,2,3]), 3)
        self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)
    
if __name__ == '__main__':
    unittest.main()