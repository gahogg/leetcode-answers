# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = Solution.as_stack(l1)
        s2 = Solution.as_stack(l2)
        ret_val = 0

        while s1 or s2:
            if len(s1) == len(s2):
                ret_val += int("".join(s1)) + int("".join(s2))
                break
            elif len(s1) > len(s2):
                ret_val += (10 ** (len(s1) - 1)) * int(s1.pop(0))
            else:
                ret_val += (10 ** (len(s2) - 1)) * int(s2.pop(0))

        ret_val_stk = [int(char) for char in str(ret_val)]
        head = ListNode(ret_val_stk.pop())
        cur = head

        while ret_val_stk:
            cur.next = ListNode(ret_val_stk.pop())
            cur = cur.next

        return head

    @staticmethod
    def as_stack(ln):
        stk = []

        while ln:
            stk.insert(0, str(ln.val))
            ln = ln.next

        return stk