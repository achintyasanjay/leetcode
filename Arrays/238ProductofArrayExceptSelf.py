class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to 
        the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        :param nums: List of integers
        :type nums: List[int]
        :return: List where each element is the product of all elements in nums except itself
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix  # Store the product of all elements to the left
            prefix *= nums[i]   # Update prefix for the next iteration
        
        # Calculate suffix products and combine with prefix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix  # Multiply by the product of all elements to the right
            postfix *= nums[i]    # Update suffix for the next iteration
        
        return result

# Time Complexity: O(n), where n is the length of nums
# - We perform two passes through the array, each taking O(n) time.
# Space Complexity: O(1), excluding the output array
# - We use only a constant amount of extra space for variables.
# Note: The result array is not considered in the space complexity as it's the required output.