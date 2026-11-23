# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:


    
        # Map each value to its index in inorder for O(1) lookup
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the subtree
            if left > right:
                return None
            
            # The last element in postorder is the root of the current subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Find the split index in inorder
            mid = inorder_idx[root_val]
            
            # IMPORTANT: Build right subtree before left subtree because
            # postorder popped from the end gives: Root -> Right -> Left
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)