# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        l = head
        r = head
        while n > 0:
            r = r.next
            n -= 1
        while r:
            prev = l
            l = l.next
            r = r.next
        if not prev:
            if not l.next:
                return None
            else:
                return l.next
        else:
            prev.next = l.next
        return head