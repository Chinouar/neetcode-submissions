# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        prev = None
        while sec:
            nex = sec.next
            sec.next = prev
            prev = sec
            sec = nex
        sec = prev

        first = head
        while sec:
            t1, t2 = first.next, sec.next
            first.next = sec
            sec.next = t1
            first,sec = t1, t2