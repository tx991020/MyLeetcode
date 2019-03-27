



class LRU:
    def __init__(self,cacheSize):
        self.cacheSize = cacheSize
        self.queue = []
        self.hashSet = set()

    def isQueueFull(self):
        return len(self.queue)== self.cacheSize

    def enqueue(self,pageNum):
        if self.isQueueFull():
            self.hashSet.remove(self.queue[0])
        self.queue.append(pageNum)
        self.hashSet.add(pageNum)

    def accessPage(self,pageNum):
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.index(pageNum,0)
    def printQueue(self):
        while len(self.queue):
            print(self.queue.popleft())



