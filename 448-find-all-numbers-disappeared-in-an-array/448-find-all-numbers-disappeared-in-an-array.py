class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        serial=[]
        nums_set=set(nums)
        n=len(nums)
        for i in range(n):
            serial.append(i+1)
        serialSet=set(serial)
        return serialSet.difference(nums_set)
            
            
        
        