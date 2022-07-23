class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[""]
        
        left=['(' , '{' , '[']
        
        right=[')', '}' , ']']
        
        for i in s:
            if i in left:
                s1.append(i)
            elif s1[-1]=='(' and i==')' :
                s1.pop()
            elif s1[-1]=='{' and i== '}':
                s1.pop()
            elif s1[-1]=='[' and i== ']':
                s1.pop()
            elif i in right:
                s1.append(i)
        if s1==[""]:
            return True
            
                
        


        
    
       
       

         
        
