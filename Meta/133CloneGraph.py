# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a copies dict to map old node to new nodes
        # Start off with root node and add to the queue
        # Start BFS and traverse neighbors for each old node
        # For each neighbor that isn't in the copies list, 
        # create a new node and map old node to new val and add to queue
        # For all the neighbors for each old node in dict, 
        # append the neighbor values (new) 
        # Return the dict with the root
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
        