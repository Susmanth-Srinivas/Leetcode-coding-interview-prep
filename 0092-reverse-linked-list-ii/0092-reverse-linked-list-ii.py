# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0,head)

        before = dummy 
        for _ in range(left-1):
            before = before.next
        
        prev = None
        curr = before.next
        for _ in range(right- left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        before.next.next = curr
        before.next = prev

        return dummy.next