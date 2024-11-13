class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # We can approach this using binary search to get logn time
        # Every time we cut our search in half we check if our missing count is greater/lower than k
        # Missing count can be calculated as arr[i] - (i + 1) which properly accounts for the amount of missed int
        # If missing count is less than k then it means that kth positive integer missing is on the right
        # Else it's on the left


        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            missing_count = arr[mid] - (mid + 1)

            if missing_count < k:
                l = mid + 1
            else:
                r = mid - 1

        return l + k

# Time: O(logn)
# Space: O(1)