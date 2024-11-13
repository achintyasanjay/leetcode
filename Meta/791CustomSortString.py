from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Use Counter to count frequencies of character in s
        # Iterate through each character in order and if it's in s, append character * frequency seen in s
        # Delete the key,val pair after done appending
        # Append remaining characters and convert to string
        freq = Counter(s)
        res = []
        for char in order:
            if char in freq:
                res.append(char * freq[char])
                del freq[char]
            
        for char, count in freq.items():
            res.append(count * char)

        return "".join(res)

# Time: O(n + m) n elements in order and m elements in s
# Space: O(m) m elements in s
