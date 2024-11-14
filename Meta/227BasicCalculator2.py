class Solution:
    def calculate(self, s: str) -> int:
        # Create a stack to store all computed numbers
        # For addition/substraction append pos/neg numbers to stack
        # For multiply/divide append computation completed nums to stack
        # Reset num after every computation and update last sign so numbers know what to do
        # Sum stack values at the end to get the answer
        stk = []
        curr_num = 0
        last = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            if i == len(s) - 1 or char in '+-*/':
                if last == '+':
                    stk.append(curr_num)
                elif last == '-':
                    stk.append(-curr_num)
                elif last == '*':
                    stk.append(stk.pop() * curr_num)
                elif last == '/':
                    stk.append(int(stk.pop() / curr_num))
                curr_num = 0
                last = char
        return sum(stk)


# Time: O(n) for iterating through entire string of characters n
# Space: O(n) worst case stores every single integer being added or subtracted