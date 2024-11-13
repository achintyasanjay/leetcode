# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
from collections import deque
from typing import List
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        # Treat this as a graph function where each array is a directed edge away from base value
        # Apply BFS to traverse graph
        # Start off with traversing the array once to start off at depth 1
        # Each time we move one level deeper keep track as second part of queue element
        # Sum up total and return

        q = deque
        q = [[elem, 1] for elem in nestedList]
        res = 0

        while q:
            element, value = q.pop()
            if element.isInteger():
                res += value * element.getInteger()
            else:
                for new in element.getList():
                    q.append([new, value + 1])
                
        return res
        # Time: O(N)
        # Space: O(W) for width
    
        # DFS Implementation
        # Create DFS function to recurse to max depth while summing integer values
        # Check if integer, if true sum it and if false dive another level
        # Start off with calling dfs function on input list
        total = 0
        def dfs(element, depth):
            nonlocal total
            for elem in element:
                if elem.isInteger():
                    total += elem.getInteger() * depth
                else:
                    total = dfs(elem.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)

        # Time: O(N)
        # Space: O(D) for depth

    

