"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # Append the first row and remove it
            result += matrix[0]
            matrix.pop(0)
            if matrix and matrix[0]:
                # Append the last element of each remaining row
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                # Append the last row in reverse and remove it
                result += matrix[-1][::-1]
                matrix.pop()
            if matrix and matrix[0]:
                # Append the first element of each remaining row in reverse
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result
              
