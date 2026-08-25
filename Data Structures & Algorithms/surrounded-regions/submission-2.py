from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        
        # marks un-surroundable elements as 2
        def bfs(i, j):
            if board[i][j] != 'O':  return

            q = deque()
            q.append((i, j))
            board[i][j] = '2'
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:
                length = len(q)
                ii, jj = q.popleft()
                
                for di, dj in directions:
                    r, c = di + ii, dj + jj
                    if 0<=r<n and 0<=c<m and board[r][c] == 'O':
                        board[r][c] = '2'
                        q.append((r, c))
        
        un_surroundable_elems = []
        for i in range(n):
            if board[i][0] == 'O':  un_surroundable_elems.append((i,0))
            if board[i][m-1] == 'O':  un_surroundable_elems.append((i,m-1))
        
        for j in range(m):
            if board[0][j] == 'O':  un_surroundable_elems.append((0,j))
            if board[n-1][j] == 'O':  un_surroundable_elems.append((n-1,j))
        
        for i, j in un_surroundable_elems:  bfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O': board[i][j] = 'X'
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '2': board[i][j] = 'O'