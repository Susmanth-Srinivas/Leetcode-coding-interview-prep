# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        def dfs(node: TreeNode | None, remaining: int) -> None:
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Must be a leaf node (no children) and match the target sum
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])

            dfs(node.left, remaining)
            dfs(node.right, remaining)

            # Backtrack
            path.pop()

        dfs(root, targetSum)
        return res