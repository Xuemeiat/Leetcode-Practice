'''
Problem: Palindrome number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Topic: numbers, strings
'''

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x //= 10
        return x == reversed or x == reversed // 10


if __name__ == "__main__":
    sol = Solution()
    num = 389834
    result = sol.isPalindrome(num)
    print(result)