# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], max_yet: int, min_yet: int) -> bool:
            if not root: return True
            if min_yet < root.val < max_yet:
                return dfs(root.left, root.val, min_yet) and dfs(root.right, max_yet, root.val) 
            
            return False
        
        return dfs(root, float('inf'), float('-inf'))