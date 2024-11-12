from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        # Initialize queue to hold moving total numbers, size, and total 
        self.q = deque()
        self.size = size
        self.total = 0

        
    def next(self, val: int) -> float:
        # Iterate through and calculate averages but pop from queue when size of q gets larger than allowed
        self.q.append(val)
        self.total += val
        if self.size < len(self.q):
            self.total -= self.q.popleft()
        return self.total / len(self.q)

# Time: O(1) 
# Space: O(n) size of moving average
