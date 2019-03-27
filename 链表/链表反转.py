
class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def reverse(self, head):
        cur, pre = head, None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre