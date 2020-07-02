# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rangeSumBST(self, root, L, R):
        return Solution.helper(root, L, R)
    
    def helper(root, L, R):
        if root is None:
            return 0
        elif (root.val >= L) and (root.val <= R):
            return Solution.helper(root.left, L, R) + Solution.helper(root.right, L, R) + root.val
        elif root.val < L:
            return Solution.helper(root.right, L, R)
        else:
            return Solution.helper(root.left, L, R)