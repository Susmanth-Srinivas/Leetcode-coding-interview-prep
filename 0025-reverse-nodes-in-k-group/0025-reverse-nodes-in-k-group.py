class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Step 1: check if k nodes exist starting from groupPrev.next
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes left, we're done

            groupNext = kth.next  # node right after this group

            # Step 2: reverse the group [groupPrev.next ... kth]
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Step 3: reconnect
            tmp = groupPrev.next      # this is now the tail of the reversed group
            groupPrev.next = kth      # kth is now the head of the reversed group
            groupPrev = tmp           # move groupPrev to the new tail for the next iteration