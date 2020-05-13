# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            # tmp.next = None
            # pre.next = head.next
            # pre.next.next = tmp    
            # head = head.next

            print(cur)


        return pre
