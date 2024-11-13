from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums so in order
        # Iterate through each num with i
        # Set left, and right pointers to check other two possible integers and close in on the middle
        # Append triplet when total == 0
        # Skip over duplicates with each i iteration and each time you find a valid triplet
        # If total too large, move right, if too small move left
        # Repeat for each iteration of i
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            total = 0
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res

# Time: O(n^2)
# Space: O(1) considered part of output