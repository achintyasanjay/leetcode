class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create left and right pointers
        # Iterate towards the middle until both pointers are at a letter
        # Compare letters and if not equal return false
        # Increment pointers once again and repeat process

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

# Time: O(n) for n elements in s
# Space: O(1) constant