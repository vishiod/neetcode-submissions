class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        
        def backtrack(open_count, close_count):
            if len(sol) == 2*n:
                res.append("".join(sol))
                return
            
            if open_count > close_count:
                sol.append(")")
                backtrack(open_count, close_count + 1)
                sol.pop()
            
            if open_count < n:
                sol.append("(")
                backtrack(open_count + 1, close_count)
                sol.pop()
        
        backtrack(0, 0)
        return res