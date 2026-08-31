class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)

        def dp(x):
            if x == 0 or x == 1:    return 1
            if cache[x] != -1: return cache[x]
            cache[x] = dp(x-1) + dp(x-2)
            return cache[x]
        
        return dp(n)