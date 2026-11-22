# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def build(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal preorder_idx

            if in_left > in_right:
                return None

            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)

            mid = inorder_index_map[root_val]

            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)

            return root

        return build(0, len(inorder) - 1)