class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Use stack to keep track of open and closed parentheses
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