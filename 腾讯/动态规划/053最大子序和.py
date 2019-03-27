'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''



'''
动态规划（只关注：当然值 和 当前值+过去的状态，是变好还是变坏，一定是回看容易理解）
ms(i) = max(ms[i-1]+ a[i],a[i])
到i处的最大值两个可能，一个是加上a[i], 另一个从a[i]起头，重新开始。可以AC
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        for i in range(1, n):
            maxSum[i] = max(maxSum[i - 1] + nums[i], nums[i])
        return max(maxSum)
'''


'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, max_end = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_end = max(max_end + nums[i], nums[i])
            max_sum = max(max_sum, max_end)
        return max_sum
'''