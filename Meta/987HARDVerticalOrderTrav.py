# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use BFS to traverse all of the nodes
        # Create dictionary to store nodes based on columns
        # Traverse through all nodes checking left and right
        # Sort cols based on column index keys
        # Create res array and iterate through the keys
        # Based on the keys (cols) sort nodes within each column
        # Append to result every iteration
        store = defaultdict(list)
        q = deque()
        q.append((0, 0, root))

        while q:
            row, col, node = q.popleft()
            if node:
                store[col].append((row, node.val))
                q.append((row + 1, col - 1, node.left))
                q.append((row + 1, col + 1, node.right))
            
        sorted_cols = sorted(store.keys())
        res = []

        for col in sorted_cols:
            store[col].sort(key= lambda x: (x[0],x[1]))
            res.append([val for row,val in store[col]])

        return res

# Time: O(nlogn) for each node in tree and sorting
# Space: O(n) for each node in tree
