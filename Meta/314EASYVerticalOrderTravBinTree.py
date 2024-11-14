# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        # Check if empty root
        # Create a dictionary to store all the nodes in the tree
        # Make sure to store the nodes by having a column counter where root is 0 and any column left is -1 and right is +1
        # Have a min and max column counter so you can iterate with bounds when appending to results array at the end from the store dictionary
        # Use a queue to visit every node traversing down the tree
        if not root:
            return []
        q = deque()
        q.append((0, root))
        store = defaultdict(list)
        min_val = float('inf')
        max_val = float('-inf')

        while q:
            col, node = q.popleft()
            store[col].append(node.val)
            
            min_val = min(min_val, col)
            max_val = max(max_val, col)
            if node.left:
                q.append((col - 1, node.left))
            if node.right:
                q.append((col + 1, node.right))

        res = []
        for i in range(min_val, 1 + max_val):
            res.append(store[i])

        return res
    
# Time: O(N) iterates through entire tree with n nodes
# Space: O(N) store holds all the node values
