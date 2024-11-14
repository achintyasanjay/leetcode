from collections import Counter
from heapq import heappop, heappush
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to get frequency of numbers in array
        # Use minheap to keeep track of the frequency of each number
        # If len of heap becomes larger than k, start popping

        min_heap = []
        freq = Counter(nums)

        for val, count in freq.items():
            heappush(min_heap, (count, val))

            if len(min_heap) > k:
                heappop(min_heap)

        return [val for _, val in min_heap]

# Time: O(nlogk) for n nums in list and k size of heap
# Space: O(n) for frequency map