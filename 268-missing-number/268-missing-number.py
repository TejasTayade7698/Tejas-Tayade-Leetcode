class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        serial=[i for i in range(0,n+1)]
        for i in serial:
            if i not in nums:
                return i
       
        


         
            
            
  
            
            