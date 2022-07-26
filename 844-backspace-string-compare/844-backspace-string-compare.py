class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        t1=[]
        for i in s:
            if i.isalpha():
                s1.append(i)
            elif len(s1)==0:
                continue
            else:
                s1.pop(-1)
        for i in t:
            if i.isalpha():
                t1.append(i)
            elif len(t1)==0:
                continue
            else:
                t1.pop(-1)
        
        while len(s1)==len(t1):
            return t1==s1  # use tuples because its ordered and duplicated allowed
        
            
        
      
              
            
        