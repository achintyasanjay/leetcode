# Definition for a Node.
from typing import List, Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create hashmap to store old nodes as keys and new nodes as values
        # First check if head exists and return None if necessary
        # Use dfs to go through the linked list
        # If there is no node or value for that node, then just return that node
        # If the node is not in the copies dictionary, create a new node with old node's val
        # Call dfs on the next node and the random node and let it go through layer and come back and return the linked list from that node
        # Call dfs starting with head and then return the dictionary starting with the head
        if not head:
            return None
        copies = {}
        def dfs(curr):
            if not curr:
                return curr
            if curr not in copies:
                copies[curr] = Node(curr.val)
                copies[curr].next = dfs(curr.next)
                copies[curr].random = dfs(curr.random)
            return copies[curr]
        dfs(head)
        return copies[head]

# Time: O(n) n nodes in list
# Space: O(n)
