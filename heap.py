
def heapify(self, data, tail_idx):
    """
    堆化内部实现
    :param data: 需要堆化的数据
    :param tail_idx: 尾元素的索引
    :return:
    """
    # heapify data[:tail_idx+1]
    if tail_idx <= 0:
        return

    # idx of the Last Parent node
    lp = (tail_idx - 1) // 2

    for i in range(lp, -1, -1):
        heap_down(data, i, tail_idx)


def heap_down(a, idx, tail_idx):
    """
    将指定的位置堆化
    :param a: 需要堆化的数据
    :param idx: a: 中需要堆化的位置
    :param tail_idx: 尾元素的索引
    :return:
    """

    lp = (tail_idx - 1) // 2
    # top-down
    while idx <= lp:
        # Left and Right Child index
        lc = 2 * idx + 1
        rc = lc + 1

        # right child exists
        if rc <= tail_idx:
            tmp = lc if a[lc] > a[rc] else rc
        else:
            tmp = lc

        if a[tmp] > a[idx]:
            a[tmp], a[idx] = a[idx], a[tmp]
            idx = tmp
        else:
            break


