# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) runtime, O(log(n)) space
    def isUnivalTree(self, root: TreeNode) -> bool:
        return Solution._helper(root, root.val)
    
    def _helper(root, val):
        if root is None:
            return True
        elif root.val != val:
            return False
        else:
            return Solution._helper(root.left, val) and Solution._helper(root.right, val)