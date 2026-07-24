# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def height(root: Optional[TreeNode]) -> int:
            if not root:   return 0
            nonlocal is_balanced
            left_height  = height(root.left)
            if is_balanced is False:    return 0

            right_height = height(root.right)
            if abs(left_height - right_height) > 1:
                is_balanced = False
                return 0
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return is_balanced
