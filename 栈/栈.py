

import heapq
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



