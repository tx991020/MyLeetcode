'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 递归方法
        if not nums:
            return None
        mid = len(nums) // 2  # 找到中间节点
        root = TreeNode(nums[mid])  # 当前节点为根节点
        root.left = self.sortedArrayToBST(nums[:mid])  # 小于当前根节点的作为左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # 大于当前根节点的作为右子树
        return root
