from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Use a while loop to merge all n elements into num1
        # Set all pointers to the ends of the lists
        # Each time one of the lists is better add decrement by that pointer
        # Decrement the k pointer for each iteration
        # Anything left over in nums2, will just be appended to the beginning of nums1

        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Time: O(m+n) traverses both lists
# Space: O(1) constant time