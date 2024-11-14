class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert to digits
        # Create dictionary to store
        # Iterate from 9 down to curr integer checking for largest digit
        # If largest digit is found, make the swap and return
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(digits))
        return num

# Time: O(n) for every digit in number
# Space: O(n) for every digit in number
