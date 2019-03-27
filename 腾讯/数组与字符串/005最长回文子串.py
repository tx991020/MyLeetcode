'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

'''
res 代表目前最大子串的长度
start 是这一轮未重复子串首字母的 index
maps 放置每一个字符的 index，如果 maps.get(s[i], -1) 大于等于 start 的话，就说明字符重复了，此时就要重置 res 和 start 的值了，
beats 74.35%

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1)+1)
            res = max(res, i - start + 1)
            maps[s[i]] = i
        return res
'''