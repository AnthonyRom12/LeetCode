"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path[:])

            # Iterate through the remaining elements in the list
            for i in range(start, len(nums)):
                # Include the current element in the subset
                path.append(nums[i])
                # Recursively find subsets starting from the current element
                backtrack(i + 1, path)
                # Remove the current element from the path to explore other options
                path.pop()

        result = []
        backtrack(0, [])
        return result
