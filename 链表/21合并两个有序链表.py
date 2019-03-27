
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # write your code here
        if head is None or head.next is None:
            return head
        pre = head
        slow = head
        fast = head.next
        while fast  is not None:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

