from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of minimum price and maximum profit if sold on that day
        low = prices[0]
        profit = 0

        for price in prices:
            # Update if lower price
            if price < low:
                low = price
            profit = max(profit, price - low)

        return profit
# Time: O(n) for n prices
# Space: O(1) constant space
