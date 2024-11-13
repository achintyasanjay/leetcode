from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if starting point is free
        # Set up directions in for sides and diagonals
        # Create a queue and start BFS to iterate through the entire grid
        # If open spot, increase count and mark the grid with 1 to say it's blocked
        # If reach the right bottom corner, return count, else return -1 for no path
        if grid[0][0] != 0:
            return -1
        directions = ((-1,-1),(1,-1),(-1,1),(1,1),(0,-1),(-1,0),(1,0),(0,1))
        q = deque()
        q.append((0,0,1))
        count = 1

        while q:
            x,y,count = q.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return count

            for directx, directy in directions:
                newx, newy = x + directx, y + directy
                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][newy] == 0:
                    q.append((newx,newy,count + 1)) 
                    grid[newx][newy] = 1

        return -1

# Time: O(n^2) going through the entire grid
# Space: O(n^2) for deque