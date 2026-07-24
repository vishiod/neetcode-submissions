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

            left_height, right_height = height(root.left), height(root.right)
            if abs(left_height - right_height) <= 1:
                local_is_balanced = True
            else: 
                local_is_balanced = False
            
            is_balanced = is_balanced and local_is_balanced
            return 1 + max(left_height, right_height)
        
        height(root)
        return is_balanced
