# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                # move curr to the last node of this duplicate group
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # cut out the whole group
                prev.next = curr.next
            else:
                # curr is unique, keep it
                prev = prev.next

            curr = curr.next

        return dummy.next
        