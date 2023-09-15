/**
* Companies
* Given an integer array nums of unique elements, return all possible 
* subsets
* (the power set).
*
* The solution set must not contain duplicate subsets. Return the solution in any order.
*
*
*
* Example 1:
*
* Input: nums = [1,2,3]
* Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
* Example 2:
*
* Input: nums = [0]
* Output: [[],[0]]
*/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        
        backtrack(nums, 0, path, result);
        
        return result;
    }
    
    private void backtrack(int[] nums, int start, List<Integer> path, List<List<Integer>> result) {
        // Add the current path to the result
        result.add(new ArrayList<>(path));
        
        // Iterate through the remaining elements in the array
        for (int i = start; i < nums.length; ++i) {
            // Include the current element in the subset
            path.add(nums[i]);
            // Recursively find subsets starting from the current element
            backtrack(nums, i + 1, path, result);
            // Remove the current element from the path to explore other options
            path.remove(path.size() - 1);
        }
    }
}
