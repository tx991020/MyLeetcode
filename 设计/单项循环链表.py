


class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = Node



class SinCycLinkedlist(object):
    def __init__(self):
        self.head = Node

    def is_empty(self):
        return self.head == Node

    def length(self):
        if self.is_empty():
            return 0
        count =1
        cur = self.head
        while cur.next != self.head:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.head
        print(cur.item)
        while cur.next != self.head:
            cur = cur.next
            print(cur.item)


    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.head = Node
            node.next = self.head
        else:
            node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            self.head =Node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.head = Node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node


    def insert(self):
        pass
