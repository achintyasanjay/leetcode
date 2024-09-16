class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

        :param strs: List of strings to encode
        :type strs: List[str]
        :return: Encoded string
        :rtype: str
        """
        res = ""
        for word in strs:
            # Add delimiter '#', length of word, and the word itself
            res += '#' + str(len(word)) + word
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.

        :param s: Encoded string
        :type s: str
        :return: Decoded list of strings
        :rtype: List[str]
        """
        res = []
        l = 0
        while l < len(s):
            if s[l] == '#':
                r = l + 1
                # Find the end of the length indicator
                while r < len(s) and s[r].isdigit():
                    r += 1
                # Extract the length of the word
                length = int(s[l+1:r])
                # Extract the word based on its length
                word = s[r:r+length]
                res.append(word)
                # Move the pointer to the start of the next word
                l = r + length
            else:
                # Skip any unexpected characters
                l += 1
        return res

# Time Complexity:
# Encode: O(n), where n is the total number of characters in all strings
# Decode: O(n), where n is the length of the encoded string
# Both functions iterate through each character once

# Space Complexity:
# Encode: O(n), where n is the total number of characters in all strings (for the result string)
# Decode: O(n), where n is the total number of characters in all decoded strings (for the result list)
# The space used is proportional to the input size in both cases
