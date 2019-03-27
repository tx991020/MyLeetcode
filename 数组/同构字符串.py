

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))






if __name__ == '__main__':
    a = 'paple'
    b = 'title'
    print(set(zip(a,b)))


