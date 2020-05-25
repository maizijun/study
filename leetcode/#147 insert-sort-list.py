# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        root = ListNode(-99)

        while(head):
            if not root.next:
                root.next = head
                head = head.next

            else:
                ix1 = root
                ix2 = root.next

                while (ix2) & (ix2.val<=head.val):
                    ix2 = ix2.next
                    ix1 = ix1.next

                ix1.next = head
                head.next = ix2

            return root  




# ListNode{val: 4, next: ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: None}}}}

#### reference answer ####
#### 想不明白 ####
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
     	# 找个排头
        dummy = ListNode(-1)
        pre = dummy

        pre.next = ListNode(99)
        print(dummy.next.val)

        # 依次拿head节点
        cur = head
        while cur:
        	# 把下一次节点保持下来
            tmp = cur.next

            # 找到插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur
            print('pre1',dummy.val,dummy.next.val)
            
            if dummy.next.next:
                print('next2',dummy.next.next.val)
            
            print(id(pre),id(dummy))
            # pre= dummy
            cur = tmp
        return dummy.next


root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)

a = Solution()
res = a.insertionSortList(root)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val)