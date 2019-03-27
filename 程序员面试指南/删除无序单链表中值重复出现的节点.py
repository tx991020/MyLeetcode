


def removeRepeatNode2(head):
    if head == None or head.next == None:
        return head
    while head != None:
        pre = head
        cur = head.next
        while cur != None:
            if cur.val == head.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        head = head.next

