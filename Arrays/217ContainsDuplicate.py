class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an array of integers, return true if the array contains any duplicates, otherwise return false.
        
        :param nums: List of integers
        :type nums: List[int]
        :return: True if the list contains any duplicates, False otherwise
        :rtype: bool
        """
        # Check if the length of the list is equal to the length of the set of the list
        # If the length is not equal, it means there are duplicate elements
        if len(nums) != len(set(nums)):
            return True
        return False
    
# Time: O(n)
# Space: O(n)