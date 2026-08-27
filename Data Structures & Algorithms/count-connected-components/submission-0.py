class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited: return 0
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor)
            
            return 1
        
        graph = defaultdict(list)
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
        
        visited = set()
        return sum(dfs(node) for node in range(n))

