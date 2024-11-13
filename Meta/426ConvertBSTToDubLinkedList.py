# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize nodes to store first and last nodes of the circular linked list
        # Perform inorder traversal go through the graph
        # Perform inorder on the left node first visit left subtree first
        # Check if the node is the first node, if it is mark it
        # Link previous node with curr node by linking to the right
        # and link back to previous node from curr node by linking to node.left to last
        # Mark the curr node as the last node and traverse the right subtree
        # Call the function with root and let it run
        # After traversal connect first and last to make circular

        self.first = None
        self.last = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if self.last: # For every other node connection
                self.last.right = node
                node.left = self.last
            else: # If first node
                self.first = node

            self.last = node
            inorder(node.right)
        
        inorder(root)
        self.first.left = self.last
        self.last.right = self.first

        return self.first
    
# Time: O(n) nodes in the BST
# Space: O(h) recursive call stack height of the tree
