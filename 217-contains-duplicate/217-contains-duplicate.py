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

#the list(set(nums)) creates a list with no repeated elements
#if size of the new list 'unique_numbers' was same as the size of 'nums' then there were no #unique elements
#if the size reduced, then common items were eliminated. That's it.