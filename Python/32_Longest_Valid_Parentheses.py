"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize a stack with dummy value
        max_length = 0  # Initialize the max length of valid parentheses substring

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_length = max(max_length, i - stack[-1])
                    else:
                        stack.append(i)
        return max_length

