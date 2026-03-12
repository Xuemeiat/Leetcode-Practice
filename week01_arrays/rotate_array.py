'''
Problem: Rotate Array
Link: https://leetcode.com/problems/rotate-array/
Difficulty: Medium
Topic: Arrays, indexing, slicing

'''
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[-k:]
        nums[:-k]
        nums[:] = nums[-k:] + nums[:-k]

if __name__ == "__main__":
    
    sol = Solution()
    step = 12
    numbers = [1,2,3,4,5,6,7]
    sol.rotate(numbers, step)
    print(numbers)



