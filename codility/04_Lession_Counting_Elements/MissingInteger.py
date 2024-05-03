"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
import unittest

def solution(A):
    pos_A = [ele for ele in A if ele > 0] #get all positive values
    if len(pos_A) == 0:
        return 1
    pos_sorted = pos_A.sort()
    act_sort = [ele for ele in range(1, len(pos_sorted))]
    missing = set(act_sort) - set(pos_sorted)
    missing_ele = list(missing)
    return missing_ele[0] if missing_ele[0] else len(pos_sorted)+1

class testSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(solution([-2, -1, 1]), 2)
        self.assertEqual(solution([1, 2, 3]),4)
        self.assertEqual(solution([-1, -3]),1)


if __name__ == '__main__':
    unittest.main()    