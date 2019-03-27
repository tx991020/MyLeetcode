class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    def empty(self):
        if self.next == None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.next
        while p != None:
            p = p.next
            size += 1
        return size

    def push(self, e):
        p = LNode(x=e)
        p.next = self.next
        self.next = p

    def pop(self):
        tmp = self.next
        if tmp != None:
            self.next = self.next.next
            return tmp.data

        return None

    def peek(self):
        if self.next != None:
            return self.next.data
        return None


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    print(stack.peek())
    print(stack.pop())
