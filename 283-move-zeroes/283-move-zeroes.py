class Solution(object):
    def moveZeroes(self, nums):
        
        i=0
        for j in range(len(nums)):
            if nums[j]!=0 and nums[i]==0:
                nums[j] , nums[i] = nums[i] , nums[j]
            if nums[i]!=0:
                i+=1
        return nums
        
  
     
                
        