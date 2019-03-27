

from collections import deque
class stack_using_queue:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, data):
        self.queue1.append(data)

    def isEmpty(self):
        return len(self.queue1) + len(self.queue2) == 0

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")

        while len(self.queue1) > 1 :
            self.queue2.append(self.queue1.popleft())

        value = self.queue1.popleft()



def main():
    sq = stack_using_queue()
    sq.push(1)
    sq.push(2)
    print(sq.pop())




if __name__ == '__main__':

    main()