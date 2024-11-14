from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            function_id, action, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)
            
            if action == "start":
                if stack:
                    # Calculate the exclusive time for the function at top of stack
                    res[stack[-1]] += timestamp - prev_time
                # Push the curr function
                stack.append(function_id)
                # Update prev_time to curr timestamp
                prev_time = timestamp
            else:  
                last_function = stack.pop()
                # Calculate its exclusive time
                res[last_function] += timestamp - prev_time + 1
                # Update prev_time to the next timestamp 
                prev_time = timestamp + 1

        return res

# Time: O(n) where n is amount of logs
# Space: O(n) where n is amount of functions
