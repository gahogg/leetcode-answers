from functools import reduce


# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, nxt=None):
#        self.val = val
#        self.next = nxt
    
class Solution:
    def getDecimalValue(self, head):
        lst = []
        Solution.make_list(head, lst)
        lst.reverse()
        val = 0
        return sum(x * 2**i for i, x in enumerate(lst))
        
    
    @staticmethod
    def make_list(node, lst):
        if node:
            lst.append(node.val)
            Solution.make_list(node.next, lst)