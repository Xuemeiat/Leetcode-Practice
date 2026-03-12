'''
Problem: Remove duplications from sorted array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Topic: two-pointers, arrays
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0 
        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
        return write + 1
        

if __name__ == "__main__":
    sol = Solution()
    numbers = [0,2,2,3]
    k = sol.removeDuplicates(numbers)
    print(k)
    print(numbers[:k])