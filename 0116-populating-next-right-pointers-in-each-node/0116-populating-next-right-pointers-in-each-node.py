"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root

        while leftmost.left:

            node = leftmost

            while node:

                # Connect siblings
                node.left.next = node.right

                # Connect children across parents
                if node.next:
                    node.right.next = node.next.left

                # Move to next parent on this level
                node = node.next

            # Move to the next level
            leftmost = leftmost.left

        return root
