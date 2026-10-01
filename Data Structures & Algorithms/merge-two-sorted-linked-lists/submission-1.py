# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def prettyprint(l: Optional[ListNode]):
    tmp = l
    while tmp:
        print(tmp.val)
        tmp = tmp.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val: 
            res = list1
            res2 = list2
        else:
            res = list2
            res2 = list1
        r = res
        tmp2 = res2
        while res.next and tmp2:
            if res.next.val >= tmp2.val:
                t = tmp2
                tmp2 = tmp2.next
                t.next = res.next
                res.next = t
                res = res.next
            else:
                res = res.next
        while tmp2:
            res.next = tmp2
            res = res.next
            tmp2 = tmp2.next
        return r