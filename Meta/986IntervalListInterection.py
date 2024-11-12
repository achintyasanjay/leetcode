from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Iterate through both lists and check the starts and ends of each interval pair
        # If end of 1 is before start of second then skip start of second
        # If start of 1 is before start of second, skip to start of second
        # Once recording check whichever end comes first and skip to that
        # Repeat process

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