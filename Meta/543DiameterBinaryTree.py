# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create dfs to check height of all nodes
        # Max distance is calculated but traversing all the way down to the each node
        # Each iteration returns the max of left and right and adds 1 for curr node
        diameter = 0
        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)
            return max(left,right) + 1
        
        dfs(root)
        return diameter

# Time: O(n) to get to each node
# Space: O(h) for tallest height in the tree      
            