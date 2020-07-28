# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) runtime, O(1) space
    def middleNode(self, head: ListNode) -> ListNode:
        num_nodes = 0
        cur = head
        while cur:
            num_nodes += 1
            cur = cur.next
        
        mid = (num_nodes // 2) + 1
        cur = head
        node_num = 1
        while node_num != mid:
            node_num += 1
            cur = cur.next
        
        return cur
        