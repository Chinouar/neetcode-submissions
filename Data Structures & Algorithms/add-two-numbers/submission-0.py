# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        i = 0
        while l1:
            n1 += l1.val * pow(10, i)
            i += 1
            l1 = l1.next
        i = 0
        while l2:
            n2 += l2.val * pow(10, i)
            i += 1
            l2 = l2.next
        r = n1 + n2
        res = ListNode(0, None)
        tmp = res
        while r > 0:
            tmp.val = r % 10
            r = r // 10
            if r <= 0:
                break
            tmp.next = ListNode(0,None)
            tmp = tmp.next
        return res