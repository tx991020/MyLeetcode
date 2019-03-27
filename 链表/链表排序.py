'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        fast = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
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