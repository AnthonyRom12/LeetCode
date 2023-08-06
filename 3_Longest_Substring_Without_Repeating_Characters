"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, temp = 0, 0
        new_array = []
        for i in s:
            while i in new_array:
                new_array.pop(0)
                temp -= 1
            else:
                new_array.append(i)
                temp += 1
                count = max(count, temp)
        return count
