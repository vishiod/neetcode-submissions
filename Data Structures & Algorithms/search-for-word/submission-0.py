class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        if m == 1 and n == 1: return board[0][0] == word

        def backtrack(i, j, index):
            if index == len(word):   return True
            if i < 0 or j < 0 or i >= n or j >= m or index > len(word):    return False
            if word[index] != board[i][j]:  return False

            cache = board[i][j]
            board[i][j] = '*'

            for ii, jj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r, c = ii + i, jj + j
                if r < 0 or c < 0 or r >= n or c >= m:  continue
                if backtrack(r, c, index + 1):  
                    board[i][j] = cache
                    return True

            board[i][j] = cache       
            return False

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):  return True
        
        return False
            

