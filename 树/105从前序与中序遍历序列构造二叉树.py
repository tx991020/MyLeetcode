'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''



'''
一句话，看到树🌲就要想到递归

preorder 是 根 -> 左 -> 右
inorder 是 左 -> 根 -> 右
首先pre的第一个就是整个树的root, 假设 preorder[0] = inorder[k],那么inorder的前k-1个就是树的左子树，后面部分就是树的右子树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        k = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:k+1], inorder[0:k])
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        return root