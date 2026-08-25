class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:   graph[course].append(pre)
        state = [0] * numCourses

        # 0=unvisited, 1=visiting, 2=visited
        def dfs(node):
            if state[node] == 1:    return False
            if state[node] == 2:    return True
            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):    return False
            
            state[node] = 2
            return True
        
        for course in range(numCourses):    
            if not dfs(course): return False

        return True