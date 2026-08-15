class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol, res, n = [], [], len(candidates)

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if i == n or curr_sum > target: return
            
            j = i
            while j < n and candidates[j] == candidates[i]:
                j+= 1

            backtrack(j, curr_sum)
            
            if curr_sum + candidates[i] <= target:
                sol.append(candidates[i])
                backtrack(i+1, candidates[i] + curr_sum)
                sol.pop()
        
        backtrack(0, 0)
        return res