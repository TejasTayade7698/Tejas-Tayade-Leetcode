class Solution(object):
    def isAnagram(self, s, t):
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        return cnt1 == cnt2
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i=(0,range(len(s)))
        # while i in range(len(s)):
        #     if s.count(s[i])==t.count(s[i]):
        #         return True
        #     else:
        #         return False
       
                