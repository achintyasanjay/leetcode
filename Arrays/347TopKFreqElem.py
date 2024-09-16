from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        :param nums: List of integers
        :type nums: List[int]
        :param k: Number of most frequent elements to return
        :type k: int
        :return: List of k most frequent elements
        :rtype: List[int]
        """
        # Count frequencies
        # Step 1: Count the frequency of each number in the input list
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Create buckets where index represents frequency
        # Initialize a list of empty lists, with length nums + 1 to account for 0 frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            # Append each number to the list at index equal to its frequency
            freq[count].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        # Iterate from highest possible frequency (len(nums)) to lowest (1)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                # Add numbers to result, starting from highest frequency
                result.append(num)
                # Check after each addition if we've reached k elements
                if len(result) == k:
                    # Return immediately when we have our k most frequent elements
                    return result

# Time Complexity: O(n)
# - Counting frequencies: O(n) as we iterate through the input list once
# - Creating buckets: O(n) as we iterate through the count dictionary
# - Collecting top k elements: O(n) in worst case, but often less in practice
# Overall: O(n) as all steps are linear

# Space Complexity: O(n)
# - count dictionary: O(n) in worst case where all elements are unique
# - freq list: O(n) as it has at most n+1 buckets
# - result list: O(k), which is O(n) in worst case where k = n
# Overall: O(n) as all data structures are at most linear in size
