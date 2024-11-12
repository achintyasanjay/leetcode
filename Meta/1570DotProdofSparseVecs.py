from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        # Create dictionary to hold index and value of all non_zero nums
        # Important preprocessing step
        self.store = {}
        for index,val in enumerate(nums):
            if val == 0:
                continue
            self.store[index] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # Check for smaller dictionary and iterate through those keys and multiple with keys of other dictionary
        # Multiply and sum up total to return
        res = 0
        if len(self.store) < len(vec.store):
            for key in self.store.keys():
                if key in vec.store:
                    res += self.store[key] * vec.store[key]
        else:
            for key in vec.store.keys():
                if key in self.store:
                    res += self.store[key] * vec.store[key]
        return res
        
# Time: O(N) for length n of input array
# Space: O(L) for L nonzero characters

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)