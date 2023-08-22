# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if x not in range(-9,9):
            x = int(str(x)[::-1].lstrip('0')) if x >= 0 else int(f"-{str(x)[:0:-1]}".lstrip('0'))
        return x if (2 ** 31 - 1 > x > -2 ** 31) else 0

obj = Solution()
print(obj.reverse)
