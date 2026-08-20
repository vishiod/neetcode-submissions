class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        max_count = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:  return 0
            if grid[i][j] != 1:   return 0
            grid[i][j] = 2
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    max_count = max(count, max_count)
        
        return max_count