# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        # Use BFS to traverse through the graph
        # Append the last value in each level to the result
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if i == level_len - 1:
                    # print("hi")
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

# Time: O(n)
# Space: O(n)