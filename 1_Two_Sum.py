"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number = target - nums[i]
            if number in nums:
                try:
                    s = nums.index(number)
                    if i != s:
                        return [i, s]
                except ValueError as e:
                    continue
        return []


obj = Solution()
print(obj.twoSum)
