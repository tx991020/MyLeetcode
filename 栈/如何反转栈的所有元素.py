
# 列表实现
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



def moveBottenToTop(s):
    if s.isEmpty():
        return
    top1 = s.peek()
    s.pop()
    if not s.isEmpty():
        moveBottenToTop(s)
        top2 = s.peek()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)

def reverse(s):
    if s.isEmpty():
        return
    moveBottenToTop(s)
    top = s.peek()
    s.pop()
    reverse(s)
    s.push(top)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    while not s.isEmpty():
        print(s.pop())