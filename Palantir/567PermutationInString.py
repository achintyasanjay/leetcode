"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2."""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a counter for the characters in s1
        s1_counter = Counter(s1)
        
        # Initialize variables
        window_size = len(s1)  # Size of the sliding window, equal to length of s1
        matches = 0  # Number of characters in the current window that match s1 in both identity and frequency
        window_counter = Counter()  # Counter for characters in the current window
        
        # Initialize the first window
        for i in range(min(len(s2), window_size)):
            if s2[i] in s1_counter:
                window_counter[s2[i]] += 1
                # If the count of this character in the window matches s1, increment matches
                if window_counter[s2[i]] == s1_counter[s2[i]]:
                    matches += 1
        
        # Check if the initial window matches s1
        if matches == len(s1_counter):
            return True  # All characters match in both identity and frequency
        
        # Slide the window through the rest of s2
        for i in range(window_size, len(s2)):
            # Remove the leftmost character from the window
            if s2[i - window_size] in s1_counter:
                # If this character's count matched s1 before removal, decrement matches
                if window_counter[s2[i - window_size]] == s1_counter[s2[i - window_size]]:
                    matches -= 1
                window_counter[s2[i - window_size]] -= 1
            
            # Add the new rightmost character to the window
            if s2[i] in s1_counter:
                window_counter[s2[i]] += 1
                # If this character's count now matches s1, increment matches
                if window_counter[s2[i]] == s1_counter[s2[i]]:
                    matches += 1
            
            # Check if the current window matches s1
            if matches == len(s1_counter):
                return True  # All characters match in both identity and frequency
        
        # If no matching window is found, return False
        return False
    
    # Time Complexity: O(n), where n is the length of s2. We only iterate through s2 once.
    # Space Complexity: O(1) - We are using a fixed amount of extra space (the counters) that does not grow with the input size.
            
            
        
