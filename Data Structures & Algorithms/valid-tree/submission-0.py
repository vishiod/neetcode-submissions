class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for node, child in edges:
            graph[node].append(child)
            graph[child].append(node)

        UNVISTIED, VISITING, VISITED = 0, 1, 2
        state = [UNVISTIED] * n

        def dfs(node, parent):
            if state[node] == VISITING: return False
            if state[node] == VISITED: return True
            state[node] = VISITING

            for child in graph[node]:
                if child == parent: continue
                if not dfs(child, node):  return False
            
            state[node] = VISITED
            return True
        
        if not dfs(0, -1):  return False
        return all(s == VISITED for s in state)



