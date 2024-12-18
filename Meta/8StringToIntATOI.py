class Solution:
    def myAtoi(self, s: str) -> int:
        # Get rid of leading whitespace
        # Check for sign by checking first index in string
        # Read in the digits through a while loop and append to total
        # Apply the sign and then check if it's within bounds
        # If smaller, return intmin if larger return intmax
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        result = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result *= sign
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

# Time: O(n) for n elements in string
# Space: O(1) for constant memory