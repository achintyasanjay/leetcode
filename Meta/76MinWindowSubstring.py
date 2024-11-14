from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a freq counter for the char in t and get length of the dict
        # Create vars for sliding window like window_count for freq
        # Create two points l and r and a counter for matched letters
        # Keep track of the min length
        # Iterate through s checking if freq in window_count and t count are the same
        # Once they are the same find min window size by making it smaller
        # Return min window substring using the indices that were kept track of
        if not s or not t:
            return ""
        
        target_count = Counter(t)
        required = len(target_count)
        
        window_count = defaultdict(int)
        left, right = 0, 0
        formed = 0
        min_length = float('inf')
        min_window = (0, 0)
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)
                
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
            right += 1
        
        if min_length == float('inf'):
            return ""
        return s[min_window[0]:min_window[1] + 1]

# Time: O(s + t) for len of s and creating freq dict
# Time: O(s) for len of s