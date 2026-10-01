# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = y = head
        while y and y.next:
            x = x.next
            y = y.next.next
            if x is y:
                return True
        return False