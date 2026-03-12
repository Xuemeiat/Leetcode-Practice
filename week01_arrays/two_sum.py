"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Arrays, Hash Map
"""
from typing import List

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return[lookup[diff], i]
            lookup[num] = [i]
        
        

if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2,6,8], 10)
    print(result)
