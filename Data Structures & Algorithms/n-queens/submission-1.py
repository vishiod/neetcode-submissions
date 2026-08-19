class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag_1 = set() # r - c
        diag_2 = set() # r + c
        res = []
        board = [["."] * n for _ in range (n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r-c) in diag_1 or (r+c) in diag_2:
                    continue
                
                col.add(c)
                diag_1.add(r-c)
                diag_2.add(r+c)
                board[r][c] = 'Q'

                backtrack(r+1)

                col.remove(c)
                diag_1.remove(r-c)
                diag_2.remove(r+c)
                board[r][c] = '.'
        
        backtrack(0)
        return res