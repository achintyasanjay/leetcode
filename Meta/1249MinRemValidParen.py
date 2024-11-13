class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Use a stack to keep track of parentheses
        # Iterate through appending all characters to a list 
        # If closed parenthese appear when stack is empty, don't append to list
        # At the end if there are still open parentheses, change it to an empty string
        # Concatenate what is left and remove all spaces

        stk = []
        res = list(s)
        for i in range(len(s)):
            if s[i] == ')':
                if not stk:
                    res[i] = ''
                else:
                    stk.pop()
            elif s[i] == '(':
                stk.append(i)
        
        while stk:
            res[stk.pop()] = ""

        return "".join(res)

# Time: O(n) n is number of characters in s
# Space: O(n) same as above
