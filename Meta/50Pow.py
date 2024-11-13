class Solution:
    def myPow(self, x: float, n: int) -> float:
        # take care of base cases where n is 0 or negative
        # Keep squaring the base, but when the exponent is odd multiple the result by x
        # Divide x by 2 every single iteration

        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        
        return res

# Time: O(logn) where n is exponent
# Space: O(1) constant