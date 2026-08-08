class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If it's a leaf, check if this node's value exactly finishes the sum
        if not root.left and not root.right:
            return targetSum == root.val

        # Otherwise, recurse into whichever children exist,
        # subtracting this node's value from the target
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)