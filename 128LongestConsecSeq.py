"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle edge case: if the input list is empty, return 0
        if not nums:
            return 0
        
        # Convert the input list to a set for O(1) lookup time
        num_set = set(nums)
        longest_streak = 0
        
        # Iterate through each number in the set
        for num in num_set:
            # Check if this number is the start of a sequence
            # If num-1 is not in the set, num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
        
                # Keep incrementing current_num and streak length
                # as long as the next consecutive number exists in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak if the current streak is longer
                longest_streak = max(longest_streak, current_streak)
        
        # Return the length of the longest consecutive sequence
        return longest_streak
        # Time Complexity: O(n)
        # - Creating the set: O(n)
        # - Iterating through the set: O(n)
        # - The while loop might seem like it could make it O(n^2), but each number
        #   is only visited once across all iterations of the while loop.
        # Therefore, the overall time complexity remains O(n).

        # Space Complexity: O(n)
        # - We use a set to store all numbers, which in the worst case
        #   (when all numbers are unique) will contain n elements.
        # - Other than that, we only use a constant amount of extra space.