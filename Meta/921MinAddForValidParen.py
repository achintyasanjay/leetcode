class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Use stack to keep track of open and closed parentheses
        # Use counter to count invalid parentheses
        # Iterate through the string and if you get closed before open increase the count and continue
        # If close after open, pop off the stack
        # If you get open, append to stack
        # If you have any left open, for each one increment the counter and pop until the stk is empty
        # Return count
        count = 0
        stk = []
        for i in range(len(s)):
            if s[i] == ")":
                if not stk:
                    count += 1
                    continue
                else:
                    stk.pop()
            elif s[i] == "(":
                stk.append("(")

        while stk:
            stk.pop()
            count += 1

        return count

# Time: O(n)
# Space: O(n)