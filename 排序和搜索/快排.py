from typing import List
import random


def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a) - 1)


def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)  # a[m] is in final position
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)


def _partition(a: List[int], low: int, high: int):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j


def qsort(array, l, r):
    if l >= r:
        return
    m = l
    for i in range(l + 1, r + 1):
        if array[i] > array[l]:
            m += 1
            array[i], array[l] = array[l], array[i]
    array[m], array[l] = array[l], array[m]
    qsort(array, l, m - 1)
    qsort(array, m + 1, r)


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    # assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


def shuffle(arr):
    for i in range(arr, -1, -1):
        j = random.randint(0, i + 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    # a1 = [3, 5, 6, 7, 8]
    # a2 = [2, 2, 2, 2]
    # a3 = [4, 3, 2, 1]
    # a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    # quick_sort(a1)
    # print(a1)
    # quick_sort(a2)
    # print(a2)
    # quick_sort(a3)
    # print(a3)
    # quick_sort(a4)
    # print(a4)

    # print(shuffle([1,2,3,4]))
    a = [1, 2, 3, 4]
    for i in range(a, -1, -1):
        print(i)

#
# public static void shuffle(int[] nums) {
#     Random random = new Random();
#     for (int i = nums.length - 1; i >= 0; i--) {
#         int j = random.nextInt(i + 1); // [0,i]
#         swap(nums, i, j);
#     }
# }
#
# private static void swap(int[] nums, int i, int j) {
#     int temp = nums[i];
#     nums[i] = nums[j];
#     nums[j] = temp;
# }

