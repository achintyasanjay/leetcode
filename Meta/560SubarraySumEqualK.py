from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Calculate prefix sum while iterating through the array
        # Store each prefix sum in a dictionary with that sum and it's count
        # Start off with a base case of 0 being the key and 1 being the value since there's only one way to get a 0
        # When calculating count, we subtract k from prefix sum which gives us a key with a count
        # That key tells us how many subarrays that key holds since we're subtracting k

        # Essentially it's prefix_sum + wtv number we're at = k, so subtracting by k and checking count for that value in the dictionary works
        prefix_count = defaultdict(int)
        prefix_sum = 0
        prefix_count[0] = 1
        total = 0

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_count:
                total += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] += 1

        return total

# Time: O(n) for every element in array
# Space: O(n) if every element is unique