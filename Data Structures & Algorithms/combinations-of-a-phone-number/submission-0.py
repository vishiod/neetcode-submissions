class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        map = {'2':'abc', '3': 'def',
                '4': 'ghi', '5': 'jkl', '6': 'mno',
                '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res, sol, n = [], [], len(digits)
        def backtrack(index):
            if index == n:
                res.append(sol[:])
                return
            
            for char in map[digits[index]]:
                sol.append(char) 
                backtrack(index + 1)
                sol.pop()
            
        backtrack(0)

        return ["".join(array_1) for array_1 in res]