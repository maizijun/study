# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        else:
            a,b = head,head.next
            a.next = self.swapPairs(b.next)
            b.next = a 

        return b 