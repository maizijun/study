class Solution:

    ## this code is terrific ##

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head 
            # termination.

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next  ## fast for 2steps while slow for 1step
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: 
                h.next, left = left, left.next
            else: 
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right

        return res.next
