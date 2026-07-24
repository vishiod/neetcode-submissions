# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.lca = root
        def dfs(root: TreeNode):
            if not root:    return
            self.lca = root
            if root is p or root is q:  return

            if root.val < p.val and root.val < q.val:   dfs(root.right)
            elif root.val > p.val and root.val > q.val: dfs(root.left)
            else: return
        
        dfs(root)
        return self.lca