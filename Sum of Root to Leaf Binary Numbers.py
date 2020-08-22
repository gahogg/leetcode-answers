from copy import deepcopy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# O(n) time, O(h) space
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return Solution._helper(root, [])
    
    def _helper(root, path_so_far):
        if root is None:
            return 0
        val_str = str(root.val)
        path_so_far.append(val_str)
        right = root.right
        left = root.left
        
        if (not left) and (not right):
            bin_num = ''.join(path_so_far)
            return int(bin_num, 2)
        else:
            return Solution._helper(left, deepcopy(path_so_far)) + Solution._helper(right, deepcopy(path_so_far))
  