class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add all rotten i, j to queue
        # if queue is empty return -1
        # start a counter inside q and increment on each element being processed in queue
        # each valid element is when fruit is fresh

        q = deque()
        n, m, fresh = len(grid), len(grid[0]), 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        ans = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q and fresh > 0:
            l = len(q)
            
            for _ in range(l):
                ii, jj = q.popleft()

                for di, dj in directions:
                    i, j = ii + di, jj + dj
                    
                    if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                        q.append((i, j))
                        grid[i][j] = 2
                        fresh -= 1
                
            ans += 1
        
        return ans if fresh == 0 else -1