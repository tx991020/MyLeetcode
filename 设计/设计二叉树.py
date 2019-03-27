class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        queue = [self.root]
        while queue:
            cur = queue.pop(0)

            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def bfs(self):
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur = queue.pop(0)
            print(cur.data)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.bfs()
