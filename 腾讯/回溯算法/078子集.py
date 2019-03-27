'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
每次拿一个，跟res里面的每一个已有列表取并集再次插入res中

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res.extend([tmp+[num] for tmp in res])
        return res     
思路 2

BackTrack 标准解法版

对每个元素，有两种可能，加入 cur_lst 和不加入 cur_lst，写起来思路还是很清爽的

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def search(tmp_res, idx):
            if idx == len(nums):
                res.append(tmp_res)
            else:
                search(tmp_res+[nums[idx]], idx+1)
                search(tmp_res, idx+1)

        search([], 0)
        return res
思路 3

DFS

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(depth, start, lst):
            res.append(lst)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, lst+[nums[i]])
        dfs(0, 0, [])
        return res      
'''