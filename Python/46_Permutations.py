"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
class Solution:
    def generate_permutation(self, arr, left, right, result):

        if left == right:
            result.append(arr.copy())
        else:
            for i in range(left, right + 1):
                arr[left], arr[i] = arr[i], arr[left]
                self.generate_permutation(arr, left + 1, right, result)
                arr[left], arr[i] = arr[i], arr[left]

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        self.generate_permutation(nums, 0, len(nums) - 1, permutation)
        return permutation
