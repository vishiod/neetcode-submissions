"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #  iterate and create nodes
        #  while creating nodes store mapping of old to new
        #  but do not link them
        #  once everything is created, iterate over old graph and
        #  create links

        head = node
        map_1 = {}

        # step 1 node creation
        def dfs(head):
            if not head or head in map_1:    return
            head_copy = Node(head.val)
            map_1[head] = head_copy
            
            if head.neighbors:
                for neighbour in head.neighbors:
                    dfs(neighbour)
        
        dfs(node)
        visited_copy = set()

        def dfs_copy(head):
            if not head or head in visited_copy:    return
            visited_copy.add(head)
            head_copy = map_1[head]
            head_copy.neighbors = [map_1[n] for n in head.neighbors]

            for neighbour in head.neighbors:
                dfs_copy(neighbour)
                
        dfs_copy(node)
        if node: return map_1[node]
        else:   return None
