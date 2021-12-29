class Solution(object):
    def romanToInt(self, s):
        x=list(s)
        """
        :type s: str
        :rtype: int
        """
        dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        
        z=0
        for i in range(len(x)-1):
            if dict[x[i]]<dict[x[i+1]]:
                z-=dict[x[i]]
            else:
                z+=dict[x[i]]
        return z+dict[x[-1]]
        
        