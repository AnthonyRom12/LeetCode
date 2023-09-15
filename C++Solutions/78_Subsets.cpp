/*
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
  */

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        
        backtrack(nums, 0, path, result);
        
        return result;
    }
    
    void backtrack(std::vector<int>& nums, int start, std::vector<int>& path, std::vector<std::vector<int>>& result) {
        // Add the current path to the result
        result.push_back(path);
        
        // Iterate through the remaining elements in the vector
        for (int i = start; i < nums.size(); ++i) {
            // Include the current element in the subset
            path.push_back(nums[i]);
            // Recursively find subsets starting from the current element
            backtrack(nums, i + 1, path, result);
            // Remove the current element from the path to explore other options
            path.pop_back();
        }
    }
};
