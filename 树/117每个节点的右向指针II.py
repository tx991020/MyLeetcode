'''
给定一个二叉树

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
示例:

给定二叉树，

     1
   /  \
  2    3
 / \    \
4   5    7
调用你的函数后，该二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
'''


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        res = []
        self.recurHelper(root, 0, res)
        for cur_level in res:
            for i in range(len(cur_level) - 1):
                cur_level[i].next = cur_level[i + 1]

    def recurHelper(self, root, level, res):
        if not root: return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root)
        self.recurHelper(root.left, level + 1, res)
        self.recurHelper(root.right, level + 1, res)