# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        new_num1 = int(num1)
        new_num2 = int(num2)

        result = new_num1 * new_num2
        return str(result)

sl = Solution()
print(sl.multiply)
