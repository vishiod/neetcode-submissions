import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        if k > len(heap):   return -1
        for i in range(len(nums)):
            if i == k - 1:
                return -heap[0]
            
            heapq.heappop(heap)