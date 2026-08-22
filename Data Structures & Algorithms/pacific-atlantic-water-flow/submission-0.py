class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:   return []
        n, m = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            seen = set(starts)

            while q:
                ii, jj = q.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i, j = di + ii, dj + jj
                    
                    if 0<=i<n and 0<=j<m and (i, j) not in seen and heights[ii][jj] <= heights[i][j]:
                        seen.add((i, j))
                        q.append((i, j))
            
            return seen
        
        starts_p = [(i, 0) for i in range(n)] + [(0, i) for i in range(m)]
        starts_a = [(i, m-1) for i in range(n)] + [(n-1, i) for i in range(m)]
        ans_p = bfs(starts_p)
        ans_a = bfs(starts_a)
        
        return list(ans_p.intersection(ans_a))
