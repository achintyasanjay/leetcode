class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, write a function to determine if t is an anagram of s.

        :param s: Source string
        :type s: str
        :param t: Target string
        :type t: str
        :return: True if t is an anagram of s, False otherwise
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # Create two hashmaps to keep track of the count of each character in the two strings
        countS, countT = {}, {}

        for i in range(len(s)):
            # Increment the count in the hashmap for the current character in both strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # If the two hashmaps are equal, it means the two strings are anagrams
        return countS == countT

# Time: O(n)
# Space: O(n)

# Approach: Hashmap with counters 
