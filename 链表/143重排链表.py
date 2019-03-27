'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''



'其实我们得到中间节点后问题已经快要解决了。我们可以将后面的链表reverse，然后每个一个元素去除前面的链表节点和后面的链表节点'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        def reverse(root):
            pre = None
            cur = root
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        if not head or not head.next:
            return
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        newHead = reverse(slow)
        ret = dummy = ListNode(-1)
        p1 = head
        p2 = newHead
        while p1 and p2:
            dummy.next = p1
            p1 = p1.next
            dummy = dummy.next
            dummy.next = p2
            p2 = p2.next
            dummy = dummy.next

        if p2:
            dummy.next = p2
        head.next = ret.next.next
