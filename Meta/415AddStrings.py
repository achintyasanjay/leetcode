class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Create two pointers one for each number
        # Iterate from the end and create carry var and res list
        # Convert each digit from str to int if still available in list
        # Calculate total by adding the two digits and carry
        # Divide by 10 to check for carry for next iter
        # Append the total mod 10 to get remainder and decrement pointers
        # Reverse the list and join for final number
        
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])
# Time: O(max(n,m)) where n and m are length of numbers
# Space: O(max(n,m)) for res array