class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head == None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def trvale(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self.head
        while cur:
            if cur.next == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        cur = self.head
        while cur:
            if cur.item == item:

                if cur == self.head:
                    self.head = cur.next
                    cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.prev
                    break
            else:
                cur = cur.next

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < (pos):
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


