


def removeValue2(head, num):
    if head == None:
        return head
    while head != None and head.val == num:
        head = head.next
    pre = head
    cur = head
    while cur != None:
        if cur.val == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
