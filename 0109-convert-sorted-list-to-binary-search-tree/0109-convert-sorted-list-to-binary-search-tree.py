# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Count the total number of nodes in the linked list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        self.curr = head
        
        # 2. Recursively build the BST using inorder traversal
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # First, build the left subtree
            left_child = build_bst(left, mid - 1)
            
            # Process the current node as the root
            root = TreeNode(self.curr.val)
            root.left = left_child
            
            # Advance the linked list pointer
            self.curr = self.curr.next
            
            # Finally, build the right subtree
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, size - 1)