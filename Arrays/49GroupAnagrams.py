class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Iterate through each string, sort it and if the value matches
        # add it to that key
        # Return all the values in list form 

        grouped = {}
        
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key in grouped:
                grouped[key].append(word)
            else:
                grouped[key] = [word]

        return grouped.values()
    
    # Time: O(n * nlogn)
    # Space: O(n * m) where m is the length of the longest string