class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #odds = sum(v & 1 for v in collections.Counter(s).values())
        #return len(s) - odds + bool(odds)
        
        hash=set()
        for i in s:
            if i not in hash:
                hash.add(i)
            else:
                hash.remove(i)
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
                