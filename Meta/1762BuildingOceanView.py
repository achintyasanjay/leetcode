from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Create and set a max iterating from the right
        # Only append to res when you get a max (tallest building)
        tallest = heights[-1]
        res = []
        res.append(len(heights) - 1)
        for i in range(len(heights) - 1, -1, -1):
            if tallest < heights[i]:
                res.append(i)
                tallest = heights[i]

        res.reverse()
        return res

# Time: O(n)
# Space: O(n)