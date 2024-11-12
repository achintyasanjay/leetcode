from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Start index counter at 1 for the first unique number
        # Iteratate through the list and check for unique values
        # Check that current element is different from previous unique element
        # If it is unique then increment i by one and make the unique element the same as the current
        # Essentially, you start off at index 1 and everytime you find a unique value you change the current i index and increment it, and if it's the same then j keeps going further down the list. You return i because you those are all your unique elements. Everything after i still holds duplicate

        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i

# Time: O(n) for iterate through the array
# Space: O(1) modifying in space  