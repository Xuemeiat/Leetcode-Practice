"""
Problem: Best time to buy and sell stocks
Link:
Difficulty: Easy
Topic: Arrays, Simple logic
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)
        return max_profit
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([1,5,4,6])
    print(result)