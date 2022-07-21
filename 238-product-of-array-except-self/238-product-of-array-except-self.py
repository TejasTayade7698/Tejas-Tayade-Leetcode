class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[1 for i in range(len(nums))]
        prefix=1
        for i in range(len(nums)):
            arr[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            arr[i]*=postfix
            postfix*=nums[i]
        return arr