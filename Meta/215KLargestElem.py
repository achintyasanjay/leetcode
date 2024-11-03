import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        # Create maxheap
        # Push every number in array on to heap, but only maintain length of k
        # Pop the smallest number off which heappop does natively because minheap in python
        # Return smallest element which represents kth largest element cuz heap only k elemtns deep
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, num)
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return maxheap[0]
    
# Time: O(nlogn) go through nums array and perform heap operation of log n each time
# Space: O(k) where k is passed in as an int