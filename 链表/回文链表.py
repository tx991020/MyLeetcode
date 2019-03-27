'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
思路二： 要想实现O(1)的空间复杂度，可以找到中间的节点，把linked list拆成两个部分，后半部分linkedlist reverse，然后比较两个linked list值是否相同，看例子：
'''
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True