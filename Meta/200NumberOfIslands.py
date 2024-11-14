from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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