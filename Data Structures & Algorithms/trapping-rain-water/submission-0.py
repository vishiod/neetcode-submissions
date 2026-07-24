class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        if n < 2:   return 0

        left_max, right_max = 0, 0
        l_max, r_max = [0] * n, [0] * n

        for i in range(n):
            j =  -i - 1
            l_max[i], r_max[j] = left_max, right_max
            
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j]) 

        sum = 0
        for i in range(n):
            potential = min(l_max[i], r_max[i])
            sum += max(0, potential - height[i])

        return sum

        