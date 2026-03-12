'''
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium
Topic: Kadan's algorithm, contigious subarrays
'''

from typing import List

class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        max_num = current_num = nums[0]
        for num in nums[1:]:
            current_num = max(num, current_num + num)
            max_num = max(max_num, current_num)

        return max_num

if __name__ == "__main__":
    sol = Solution()
    numbers = [-2,3,5,1,-8]
    result = sol.maxSubarray(numbers)
    print(result)

