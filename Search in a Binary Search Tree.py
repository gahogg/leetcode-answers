# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) runtime, O(n) space
    def searchBST(self, root, val):
        return Solution.search_bst(root, val)
    

    @staticmethod
    def search_bst(root, val):
        if root is None:
            return None
        else:
            if root.val == val:
                return root
            elif root.val < val:
                return Solution.search_bst(root.right, val)
            else:
                return Solution.search_bst(root.left, val)