from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Iterate through the BST, using DFS checking whether the nodes are within the low/high interval
        # If node is higher than high, only traverse left, if lower than low, traverse right
        # If within the bounds completely, check both children
        total = 0
        def recur(node):
            nonlocal total
            if not node:
                return 0

            if low <= node.val <= high:
                total += node.val
                recur(node.left)
                recur(node.right)

            elif node.val < low and node.right:
                recur(node.right)
            elif node.val > high and node.left:
                recur(node.left)
            return total
        
        recur(root)
        return total

# Time: O(n) iterating through all nodes
# Space: O(H), best - O(logN), worst O(N) for height of the tree because of the callstack