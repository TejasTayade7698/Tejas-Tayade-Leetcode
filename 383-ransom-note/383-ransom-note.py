class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """              
        dic={}
        for i in ransomNote:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        
        for i in dic:
            if magazine.count(i)<dic[i]:
                return False
        return True
        
            
        