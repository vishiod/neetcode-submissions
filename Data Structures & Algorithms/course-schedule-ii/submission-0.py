class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        UNVISITED, VISITING, VISITED = 0, 1, 2
        graph = defaultdict(list)
        state = [UNVISITED] * numCourses
        
        for course, pre in prerequisites:       
            graph[course].append(pre)
        
        def dfs(node):
            if state[node] == VISITING: return False
            if state[node] == VISITED:  return True
            
            state[node] = VISITING

            for neighbour in graph[node]:
                if not dfs(neighbour):  return False
            
            state[node] = VISITED
            order.append(node)

            return order
        
        for i in range(numCourses):
            if not dfs(i):  return []
        
        return order