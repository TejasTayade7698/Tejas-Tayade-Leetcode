class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if target in nums:
            val=nums.index(target)
            return val
        else: 
            return -1