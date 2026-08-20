class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m, ans = len(grid), len(grid[0]), 0

        def backtrack(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:  return
            if grid[i][j] != '1':    return
            
            grid[i][j] = '-1'
            backtrack(i + 1, j)
            backtrack(i, j + 1)
            backtrack(i - 1, j)
            backtrack(i, j - 1)    
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    backtrack(i, j)
                    ans += 1
        
        return ans