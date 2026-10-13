# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    h = {}
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, d, u):
            if not node:
                return True
            if not (d < node.val < u):
                return False
            return (valid(node.left,d, node.val) and valid(node.right, node.val, u))
        return valid(root, float('-inf'), float('inf'))
        