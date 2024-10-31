# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if empty root
        # Create a dictionary to store all the nodes in the tree
        # Make sure to store the nodes by having a column counter where root is 0 and any column left is -1 and right is +1
        # Have a min and max column counter so you can iterate with bounds when appending to results array at the end from the store dictionary
        # Use a queue to visit every node traversing down the tree
        if not root:
            return []
        q = deque()
        res = []
        
        q.append([0, root])
        store = defaultdict(list)
        minval = float('inf')
        maxval = float('-inf')

        while q:
            val, node = q.popleft()
            store[val].append(node.val)
            minval = min(minval, val)
            maxval = max(maxval, val)
            if node.left:
                q.append((val - 1, node.left))
            if node.right:
                q.append((val + 1, node.right))
            

        for i in range(minval, maxval + 1):
            res.append(store[i])
        return res
    
# Time: O(N) iterates through entire tree with n nodes
# Space: O(N) store holds all the node values
