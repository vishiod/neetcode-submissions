# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            if not root: return 0
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            max_sum[0] = max(max_sum[0], root.val + left_max + right_max)
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return max_sum[0]