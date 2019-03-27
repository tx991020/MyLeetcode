class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 快指针先走x步，再快慢指针同步走，快指针走到尾时，满指针在n-x, 到此时删除满指针链表的一下的节点
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy

        while n and fast:
            fast = fast.next
            n -= 1

        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next