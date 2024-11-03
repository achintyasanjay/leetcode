class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Simple binary search looking for any local peak
        # Cut array in half in the direction of ascending order
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
    
# Time: O(logN) Binary search cutting array in half each time
# Space: O(1) not data structure holding value other than integers