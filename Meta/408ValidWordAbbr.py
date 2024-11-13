class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Iterate over both strings
        # Check if digit
        # If digit, iterate through all digits converting them to integer and move index of word size forward
        # If not digit, make sure it matches as you iterate through

        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = 10 * num + int(abbr[j])
                    j += 1
                i += num
            
            else:
                if word[i] != abbr[j]:
                    print("mismatch")
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)

# Time: O(n + m) Runs through entire stack for both words
# Space: O(1) no data structure holding variable