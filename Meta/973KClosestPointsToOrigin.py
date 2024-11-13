import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Want to use a maxheap to solve this problem
        # Keep maxheap size of k and keep pushing all the negative distances because closest
        # Only the k closest distances will remain and return that in a list

        dist = []
        for x, y in points:
            distance = (x**2 + y**2)**0.5
            heapq.heappush(dist, (-distance, (x, y)))

            if len(dist) > k:
                heapq.heappop(dist)

        return [points for _, points in dist]

# Time: O(nlogk) where n is amount of points and k is size of heap
# Space: O(k) for size of heap

# Test case
solution = Solution()
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(solution.kClosest(points, k))  # Expected output: [[-2, 2], [1, 3]]