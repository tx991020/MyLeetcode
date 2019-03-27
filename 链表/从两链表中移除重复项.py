
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i


'''
输入
[2,7,11,15]
9
输出
[0,1]
预期结果
[0,1]
'''