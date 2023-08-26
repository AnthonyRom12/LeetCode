/**
 * Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
 *
 * You must implement a solution with a linear runtime complexity and use only constant extra space.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [2,2,1]
 * Output: 1
 * Example 2:
 *
 * Input: nums = [4,1,2,1,2]
 * Output: 4
 * Example 3:
 *
 * Input: nums = [1]
 * Output: 1
 *
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num: nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        int uniqueValue = 0;
        for (Map.Entry<Integer, Integer> entry: frequencyMap.entrySet()) {
            if (entry.getValue() == 1) {
                uniqueValue = entry.getKey();
                break;
            }
        } 
        return uniqueValue;
    }
}
