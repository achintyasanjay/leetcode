from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create directions for possible traversal
        # Create dfs to go to each possible location on graph
        # Start traversal by setting that location to 2 so it's visited
        # Iterate through and make sure in bounds and not visited and call again
        # Run forloop through entire graph and if that spot is 1 call dfs
        # For each time a spot is 1, its an island and return num of islands
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            grid[x][y] = "2"
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    dfs(nx, ny)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res

# Time: O(m*n) traversal of entire grid
# Space: O(m*n) for callstack 