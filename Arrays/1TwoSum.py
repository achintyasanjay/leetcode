class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        :param nums: List of integers
        :type nums: List[int]
        :param target: Target sum
        :type target: int
        :return: List containing two indices
        :rtype: List[int]
        """
        seen = {}  # dict to store the numbers we have seen so far and their indices

        for i in range(len(nums)):
            remainder = target - nums[i]  # calculate the remainder needed to reach the target

            if remainder in seen:  # if we have seen the remainder before
                return [i, seen[remainder]]  # return the current index and the index of the remainder
            else:
                seen[nums[i]] = i  # add the current number and its index to the seen dict
