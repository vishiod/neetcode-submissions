class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # step: 1 mark visited as 2
        # step: 2 dfs left, right, up and down when u r at float('inf')
        # step: 3 keep on doing it until u either find 0 or u r out of bounds or visited
        # return count in case of 0 or else return 0 from dfs so that hop count is known
        # if count is 0 then revert visited position to float('inf') or else 0

        n, m = len(grid), len(grid[0])
        q = deque()
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            di, dj = q.popleft()
            for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i, j = di + ii, dj + jj
                if 0 <= i < n and 0 <= j < m and grid[i][j] == 2147483647:
                    grid[i][j] = grid[di][dj] + 1
                    q.append((i, j))
