
'''
给定一个数组 array[1, 4, -5, 9, 8, 3, -6]，在这个数字中有多个子数组，子数组和最大的应该是：[9, 8, 3]，输出20，再比如数组为[1, -2, 3, 10, -4, 7, 2, -5]，和最大的子数组为[3, 10, -4, 7, 2]，输出18。
---------------------

'''

def maxSubArray(arr):
    if arr is None:
        return
    nAll = arr[0]
    nEnd = arr[0]
    for i in range(len(arr)):
        nEnd = max(nEnd+arr[i],arr[i])
        nAll = max(nEnd,nAll)
    return nAll



if __name__ == '__main__':
    arr = [1,-2,4,8,-4,7]
    print(maxSubArray(arr))