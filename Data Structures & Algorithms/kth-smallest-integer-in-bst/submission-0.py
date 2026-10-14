# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tr = []
        def rec(root: Optional[TreeNode]):
            if not root:
                return;
            rec(root.left)
            tr.append(root.val)
            rec(root.right)
            return;
        rec(root)
        return tr[k-1]