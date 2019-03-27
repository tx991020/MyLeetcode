'''
  二叉搜索树迭代器
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。



示例：



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false


提示：

next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            cur = self.stack.pop()
            if cur.right:
                self.pushAllLeft(cur.right)
            return cur.val

    def pushAllLeft(self, node):
        """
        :type node: TreeNode
        """
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left



