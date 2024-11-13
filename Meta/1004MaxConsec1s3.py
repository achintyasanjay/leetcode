from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window approach
        # Keep expanding until zero count goes over k, then shrink until under k
        # Keep updating max size as we iterate through the array
        left = 0
        max_len = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, r - left + 1)

        return max_len

# Time: O(n) n elements in nums
# Space: O(1) constant space
