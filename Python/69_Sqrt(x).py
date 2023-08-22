# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        result = math.sqrt(x)
        return int(result)

obj = Solution()
print(obj)
