# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        act = head
        prev = None
        while act:
            nex = act.next
            act.next = prev
            prev = act
            act = nex
        return prev