# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        small_tail = small_dummy
        big_tail = big_dummy

        curr = head
        while curr:
            if curr.val < x:
                small_tail.next = curr
                small_tail = curr
            else:
                big_tail.next = curr
                big_tail = curr

            curr = curr.next

        big_tail.next = None
        small_tail.next = big_dummy.next

        return small_dummy.next


        