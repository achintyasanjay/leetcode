class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        This function checks if a given string is a palindrome or can be converted into a palindrome by removing at most one character.
        It iterates through the string from both ends, comparing characters. If it finds a mismatch, it checks if removing one of the characters
        would result in a palindrome. If not, it returns False. If it successfully iterates through the entire string or finds a palindrome after
        removing one character, it returns True.
        """
        # Time complexity: O(n), where n is the length of the string, as we iterate through the string once.
        # Space complexity: O(1)
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1][::-1] == s[left+1:right+1]
        return True
