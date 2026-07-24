# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(root: Optional[TreeNode]) -> int:
            if not root:    return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height

            nonlocal max_diameter
            max_diameter = max(max_diameter, diameter)
            return 1 + max(left_height, right_height)
        
        height(root)
        return max_diameter
        