from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap to keep track of precomputed differences
        # Once you find a match with curr_diff to a key, return curr_index and value of key in dict (index of that val)
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [i, seen[comp]]
            seen[nums[i]] = i

# Time: O(n)
# Space: O(n)