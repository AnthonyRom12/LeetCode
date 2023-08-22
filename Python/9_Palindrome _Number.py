# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = True
        a = str(x)
        if a[:] == a[::-1]:
            return flag
        else:
            flag = False
            return flag

obj = Solution()
print(obj.isPalindrome)
        
