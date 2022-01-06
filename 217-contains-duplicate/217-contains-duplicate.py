class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_numbers = list(set(nums))
        if len(nums)==len(unique_numbers):
            return False
        else:
            return True
