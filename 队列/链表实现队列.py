class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.end = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.head
        while p != None:
            p = p.next
            size += 1
        return size

    def enQueue(self, e):
        p = LNode(x=e)

        p.next = None
        if self.head == None:
            self.head = self.end = p
        else:
            self.end.next = p
            self.end = p

    # 出队列，删除队首元素
    def deQueue(self):
        if self.head == None:
            print("队列为空")

        self.head = self.head.next
        if self.head == None:
            self.end = None

    # 取得队首元素
    def getFront(self):
        if self.head == None:
            print("获取队首元素失败")
            return None
        return self.head.data

    def getBack(self):
        if self.end == None:
            print("队列已为空")
            return None
        return self.end.data


if __name__ == '__main__':
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print(queue.getBack())
    print(queue.getFront())
