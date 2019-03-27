

class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add(self, item):
        node = LNode(item)
        node.next = self.head
        self.head = node

    def is_empty(self):
        return self.head == None

    def append(self, item):
        node = LNode(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def search(self, item):
        cur = self.head
        while not cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def reverse1(self, head):
        if head.next == None:
            return head
        new_head = self.reverse1(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverse(self, head):
        cur, pre = head, None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre

    def travel(self, head):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next







if __name__ == "__main__":
    print(int((str(3210)[::-1])))

    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)







