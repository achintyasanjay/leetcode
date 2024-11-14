from collections import defaultdict
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # We want to create a dictionary to classify each diagonal
        # Comes down to patterns with diags being either even/odd
        # We use the sum of x,y coord as key and the value as val
        # Now we have each diagonal classified into a key
        # Traverse graph and if coord is even reverse the val list
        # If odd key, then just extend list on to res

        if not mat or not mat[0]:
            return []
        
        diag = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                diag[i + j].append(mat[i][j])
        
        res = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                res.extend(reversed(diag[k]))
            else:
                res.extend(diag[k])
        return res

# Time: O(m*n) for n by m elements
# Space: O(m*n) for n by m elements
        