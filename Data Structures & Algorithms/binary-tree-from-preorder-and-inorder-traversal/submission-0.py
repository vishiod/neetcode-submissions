# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        
        pre_idx = 0
        idx_map_for_partition = {val:i for i, val in enumerate(inorder)}

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:    return
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = idx_map_for_partition[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        
        return build(0, len(preorder) - 1)