# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Keep track of order by using a minheap
        # Iterate through each list and add to minheap by the first value of each list
        # Create dummy node to return later
        # Go through minheap until empty and each iteration take the smallest node and add it to linked list
        # If there's something left in the list, then put it back on to the heap
    
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        curr = dummy
        while min_heap:
            val, index, smallest = heapq.heappop(min_heap)
            curr.next = smallest
            curr = curr.next

            if smallest.next:
                heapq.heappush(min_heap, (smallest.next.val, index, smallest.next))

        return dummy.next

# Time: O(nlogk) where n is number of lists and k is size of the heap
# Space: O(k) for size of the heap