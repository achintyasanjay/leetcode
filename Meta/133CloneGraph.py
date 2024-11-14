# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copies = {}
        q = deque([node])
        copies[node] = Node(node.val)
        
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                # If neighbor hasn't been cloned, clone and add it to the dictionary
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                # Add the cloned neighbor to the current node's clone
                copies[curr].neighbors.append(copies[neighbor])
        
        return copies[node]
        