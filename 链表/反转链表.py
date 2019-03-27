'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,data=None):
        self.val = x
        self.next = data


def reverseList1(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead


def reverseList(head):
    if head == None:
        return
    pre = None
    while head != None:

        head.next = pre
        pre = head
        head = head.next
    return pre



class Solution1(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head



def walk(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next





if __name__ == '__main__':
    a = ListNode(3,ListNode(4,ListNode(5)))

    walk(a)


