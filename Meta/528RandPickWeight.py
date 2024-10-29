import random, bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for i in range(len(w)):
            total += w[i]
            self.prefix.append(total)
        self.total = total
            
    def pickIndex(self) -> int:
        
        target = random.randint(1,self.total)
        return bisect.bisect_left(self.prefix, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Time: O(n) - prefix sum iteration
# Space: O(n) - prefix sum iteration