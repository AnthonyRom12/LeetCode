/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
  */
#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Create an unordered_map to store the complement of each number and its index
        std::unordered_map<int, int> complementMap;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int complement = target - num;

            // Check if the complement exists in the map
            if (complementMap.find(complement) != complementMap.end()) {
                // Return the indices of the two numbers that add up to the target
                return { complementMap[complement], i };
            }

            // Add the current number and its index to the map
            complementMap[num] = i;
        }

        // If no solution is found, return an empty vector or handle it as needed
        return {};
    }
};
