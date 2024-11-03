class Solution:
    def simplifyPath(self, path: str) -> str:
        # Use stack to keep track of all the components in the strin
        # Split string by slashes to get all directories
        # If single period, just skip over
        # If double period, check if anything in dir stack and pop parent directory 
        # If not space, or single or double period just keep adding to dir stack
        stk = []
        path = path.split("/")
        for elem in path:
            if stk and elem == "..":
                stk.pop()
            elif elem not in ["", ".", ".."]:
                stk.append(elem)

        return "/" + "/".join(stk)

# Time: O(n) for iterating through each character in str
# Space: O(k) for holding each directory k in stack
        