class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def arrtotree(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.arrtotree(arr[:mid])
        root.right = self.arrtotree(arr[mid + 1 :])
        return root


if __name__ == "__main__":
    a = TreeNode().arrtotree([1, 3, 2, 4])




