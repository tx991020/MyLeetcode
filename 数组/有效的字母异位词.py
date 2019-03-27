
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        chaStr = "qwertyuiopasdfghjklzxcvbnm"
        if len(s) != len(t):
            return False
        for i in chaStr:
            if s.count(i) != t.count(i):
                return False
        return True










