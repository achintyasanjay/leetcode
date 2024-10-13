class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # use a stack to keep track of current parenthese
        # iterate over all other characters that aren't parentheses
        # check at the beginning of there are no open parentheses on the stack then remove a close parenth
        # for each open you can iterate over a close and pop from the stack

        stack = []
        res = []
        invalid = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)

        while stack:
            invalid.add(stack.pop())
        
        for i in range(len(s)):
            if i in invalid:
                continue
            res.append(s[i])

        return "".join(res)