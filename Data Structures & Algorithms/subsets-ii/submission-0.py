class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol, res, n = [], [], len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            j = i
            while j < n and nums[j] == nums[i]: j+= 1
            backtrack(j)

            if i < n:
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res