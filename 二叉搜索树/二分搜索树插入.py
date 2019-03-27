
import  random
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return

    def search(self, val):
        if self is None:
            return self
        current = self
        while current and current.val != val:
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild
        return current

class binarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self.root.insert(val)

BST = binarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting  " +str(ele ) +":")
    BST.insert(ele)
