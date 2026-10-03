# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        
        def build(lo,hi):
            if lo > hi:
                return[None]

            trees = []
            for root in range(lo,hi+1):
                left_trees = build(lo,root-1)
                right_trees = build(root+1,hi)

                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(root,left,right))

            return trees

        return build(1,n)
            


