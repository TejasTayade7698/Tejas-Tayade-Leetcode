class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl=lower(s)
        i=0
        j=len(sl)-1
        while i<j:
            if not sl[i].isalnum():
                i+=1
                continue
            if not sl[j].isalnum():
                j-=1
                continue
            elif sl[i]!=sl[j]:
               
                return False
            i+=1
            j-=1
        return True
            
        