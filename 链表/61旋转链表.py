'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        ListLen = 0
        p = head
        # 数有几个节点
        while (p):
            ListLen += 1
            p = p.next

        # 优化
        k = k % ListLen
        if k == 0:
            return head

        # 快节点先走k步
        p = head
        while (k > 0):
            k -= 1
            p = p.next
        slow = head
        fast = p
        # 接着让fast走到最后一个节点，slow与它有着同样的速度
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 把头尾连起来然后断开链表
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head


class Solution1:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        if head is None:
            return None

        # 先数链表有几个节点
        i = head
        count = 1
        while i.next is not None:
            i = i.next
            count += 1
        # 抛掉重复的转圈,也算一种算法优化吧
        k = k % count
        if (k == 0) or count == 1:
            return head
        # 把链表头尾连起来
        i.next = head

        # 从dummy开始运动
        i = dummy
        # 运动到新的链表的头的上一个节点
        for _ in range(count - k):
            i = i.next

        j = i.next
        i.next = None
        return j
