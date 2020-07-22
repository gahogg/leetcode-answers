from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) runtime, O(n) space
    def increasingBST(self, root):
        sorted_queue = deque()
        Solution._build_queue(root, sorted_queue)
        head = sorted_queue.popleft()
        node = head
        while sorted_queue:
            node.left = None
            node.right = sorted_queue.popleft()
            node = node.right
        return head
            
    
    @staticmethod
    def _build_queue(root, sorted_queue):
        if not root:
            return
        Solution._build_queue(root.left, sorted_queue)
        sorted_queue.append(root)
        Solution._build_queue(root.right, sorted_queue)
    