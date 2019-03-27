

from  collections import deque

class LRU:
    def __init__(self,cacheSize):
        self.cacheSize = cacheSize
        self.queue = deque()
        self.hashSet = set()

    def isQueueFull(self):
        return self.cacheSize == len(self.queue)
