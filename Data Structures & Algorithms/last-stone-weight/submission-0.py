import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        print(heap)

        while len(heap) > 1:
            largest_elem = -1 * heapq.heappop(heap)
            second_elem = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -1 * (largest_elem - second_elem))
        
        return -heap[0]