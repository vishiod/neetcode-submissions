# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.result = None

        def dfs(root):
            if not root:    return
            if self.result is not None:    return
            
            dfs(root.left)
            self.counter += 1

            if self.counter == k:    
                self.result = root.val
                return

            dfs(root.right)

        dfs(root)
        return self.result