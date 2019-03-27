

def HalfSearch(OrderedList, key, left , right):
    if left > right:
        return None
    mid = (left + right) // 2
    if key == OrderedList[mid]:
        return mid
    elif key > OrderedList[mid]:
        return HalfSearch(OrderedList, key, mid + 1, right)
    else:
        return HalfSearch(OrderedList, key, left, mid - 1)


def BinarySearch(OrderedList, key, left, right):
    while left <= right:
        mid = (left + right) // 2
        if key == OrderedList[mid]:
            return mid
        elif key > OrderedList[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None





l =[1,3,2,2,4]


# 最简快排
def ksort(L):
    if L ==[]:
        return []
    else:
        mid = L[0]
        low = [i for i in L[1:] if i < mid]
        high = [i for i in L[1:] if i >= mid ]
        return ksort(low)+[mid]+ksort(high)






if __name__ == '__main__':
    print(ksort(l))