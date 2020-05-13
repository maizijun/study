# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ## 双指针法 1指针卡开头，1指针卡下一个不同值的索引 ##

        dummy_head = ListNode(-1)
        dummy_head.next = head

        if not head or not head.next:
            return head

        pre = head
        cur = head.next

        if pre and cur:
            print(pre.val,cur.val)
            while (pre.val == cur.val):
                cur = cur.next
                pre.next = cur     

            cur = cur.next
            pre = pre.next   

        return dummy_head.next




#### non recursive ####
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-99)
        dummy_head.next = head

        pre = dummy_head
        cur = head

        while cur:
            print(head.val,pre.val,cur.val)
            if pre and cur.val == pre.val:
                cur = cur.next
                pre.next = cur
                # cur.next = None
                # cur = pre.next
                continue

            pre = cur
            cur = cur.next

        return dummy_head.next


#### recursive ####

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        child = self.deleteDuplicates(head.next)
        if child and head.val == child.val:
            head.next = child.next
            child.next = None
            
        return head
        