# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Two pointer solution where each pointer traverses up until one pointer reaches root
        # Once it reaches root it moves pointer to where other pointer is
        # Once they both match eventually loop is broken and returned
        a,b = p,q
        while a != b:

            a = a.parent if a else q
            b = b.parent if b else p

        return a
    
    # Time: O(h) where h is height because max traversal is to root
    # Space: O(1) because only holds one value that changes