from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First we need to find the pivot where the list starts decreasing when traversing from right to left
        # If there is no pivot and it's increasing the entire way from right-left, just reverse the list in place and return
        # Once you find the pivot, we need to swap the pivot element with the next smallest integer
        # After the swap we want to make sure the reest of the list turns into ascending order from descending order
        # Reverse the suffix from the pivot element
        pivot = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot+1:] = reversed(nums[pivot+1:])

# Time: O(n) iterates through all of list worst case
# Space: O(1) modify in place