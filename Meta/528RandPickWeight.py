import random, bisect
from typing import List
class Solution:

    def __init__(self, w: List[int]):
        # Create prefix sum array to create cumulative probability elements
        # Iterate through array and add each new number to running total so the space between represented the prob
        # Keep track of total to send to pickIndex
        prefix_sum = 0
        self.prefix_arr = []
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_arr.append(prefix_sum)
        self.totalSum = prefix_sum
        print(self.prefix_arr)

    def pickIndex(self) -> int:
        # Generate random number to variability
        # Binary sort to find where the random number should be putting it to the left of the index it's supposed to be at making it fit in that range, which supports the probability being passed through
        rand_int = random.randint(1, self.totalSum)
        index = bisect.bisect_left(self.prefix_arr, rand_int)
        return index
        
# Time: O(n) for init to run through the elements in the list O(logN) for the pickIndex running binary sort
# Space: O(n) for prefix_arr to hold all the elements


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()