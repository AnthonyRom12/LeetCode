"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
    # Check if n is less or equal to 1
        if numRows <= 1:
            return s

        result = ""

        # Iterate rowNum from 0 to n - 1
        for rowNum in range(numRows):
            i = rowNum
            up = True

            # Iterate i till s.length() - 1
            while i < len(s):
                result += s[i]

                # Check if rowNum is 0 or n - 1
                if rowNum == 0 or rowNum == numRows - 1:
                    i += 2 * numRows - 2
                else:
                    if up:
                        i += 2 * (numRows - rowNum) - 2
                    else:
                        i += rowNum * 2
                    up ^= True
        return result
