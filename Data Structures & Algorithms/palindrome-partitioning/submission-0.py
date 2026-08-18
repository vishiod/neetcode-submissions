class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol, res, n = [], [], len(s)

        def isPalindrome(stringg: str):    
            return stringg == stringg[::-1]
        
        def backtrack(start):
            if start == n:  
                res.append(sol[:])
                return

            for end in range(start, n):
                piece = s[start: end + 1]
                if isPalindrome(piece):
                    sol.append(piece)
                    backtrack(end + 1)
                    sol.pop()

        backtrack(0)
        return res