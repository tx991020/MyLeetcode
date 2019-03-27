class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 已顺序数组转二分搜索树
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


# 由数组构建树
class MakeTree:
    def make(self, root, nums, i):

        if i > len(nums)-1:
            return None
        root = TreeNode(nums[i])

        root.left = self.make(root, nums, 2 * i + 1)
        root.right = self.make(root, nums, 2 * i + 2)
        return root


def order(root):
    if root is None:
        return None
    print(root.value)
    order(root.left)

    order(root.right)


def levelorder(root):
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        print(111, node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        res.append(node.value)
    return res


if __name__ == "__main__":
    a = Solution().sortedArrayToBST([1, 2, 3, 4, 5])

    # levelorder(a)
    # order(a)
    # print(levelorder(a))

    b = MakeTree().make(None,[5,4,3,2,1],0)
    order(b)
    # root = TreeNode(
    #     "D",
    #     TreeNode("B", TreeNode("A"), TreeNode("C")),
    #     TreeNode("E", right=TreeNode("G", TreeNode("F"))),
    # )
    # order(root)
    # print(levelorder(root))



def qsort(arr,l,r):
    p = partion(arr,l,r)
    qsort(arr,l,p)
    qsort(arr,p+1,r)

def partion(arr,l,r):
    j = l
    for i in range(l+1,r):
        j +=1
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

    arr[j],arr[r] = arr[r],arr[j]
    return j




