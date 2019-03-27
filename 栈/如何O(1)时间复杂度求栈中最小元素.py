class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def push(self, item):
        self.items.append(item)

    def peek(self):

        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None


class MyStack:
    def __init__(self):
        self.elemStack = Stack()
        self.minStack = Stack()

    def push(self, item):
        self.elemStack.push(item)
        if self.minStack.isEmpty():
            self.minStack.push(item)
        else:
            if item < self.minStack.peek():
                self.minStack.push(item)

    def pop(self):
        topData = self.elemStack.peek()

        self.elemStack.pop()
        if topData == self.minStack.peek():
            print(1111)
            self.minStack.pop()

        return topData

    def min(self):
        if self.minStack.isEmpty():
            return -1
        return self.minStack.peek()


if __name__ == '__main__':
    s = MyStack()
    s.push(5)

    s.pop()
    s.pop()

    print(s.min())
