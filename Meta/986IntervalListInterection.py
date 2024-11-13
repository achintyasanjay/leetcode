from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Iterate through both lists and check the starts and ends of each interval pair 
        # If start1 is before end2 and start2 is before end1, there is def overlap
        # Find the starting point using max and the ending point using min
        # Append that your result array
        # If the end of the first array is less than the end of the second move the 
        # iterator for the first array to check overlap for next list
       
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start1,end1 = firstList[i]
            start2,end2 = secondList[j]

            if start1 <= end2 and start2 <= end1:
                intersectstart = max(start1,start2)
                intersectend = min(end1,end2)
                res.append([intersectstart,intersectend])

            if end1 < end2:
                i += 1
            else:
                j += 1
        return res

# Time: O(m+n) m and n len of firstList and secondList
# Space: O(k) num of intersections found