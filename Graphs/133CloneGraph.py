
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to map original nodes to their clones
        node_map = {}
        
        def dfs(original_node):
            # If we've already cloned this node, return the clone
            if original_node.val in node_map:
                return node_map[original_node.val]
            
            # Create a new node with the same value as the original node
            clone_node = Node(original_node.val)
            # Map the original node to its clone
            node_map[original_node.val] = clone_node
            
            # Recursively clone the neighbors
            for neighbor in original_node.neighbors:
                # For each neighbor, clone it (if not already cloned) and add to the clone's neighbors
                clone_node.neighbors.append(dfs(neighbor))
            
            # Return the fully cloned node
            return clone_node

        # Time Complexity: O(N + M), where N is the number of nodes and M is the number of edges
        # We visit each node once and traverse each edge once

        # Space Complexity: O(N)
        # In the worst case, we store all nodes in the node_map
        # The recursion stack can also go up to O(N) in the worst case (for a linear graph)
        
        # Start DFS from the first node
        return dfs(node)