import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def measureDistance(x1, x2, y1, y2) -> int:
            return pow((x1-x2), 2) + pow((y1-y2), 2)
        
        heap = []
        heapq.heapify(heap)

        for point in points:
            dist = measureDistance(point[0], 0, point[1], 0)
            
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            elif -dist > heap[0][0]:
                heapq.heapreplace(heap, (-dist, point))

        return [val[1] for val in heap]