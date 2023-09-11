/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
  */
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<int> triangle;
        vector<vector<int>> result;

        for (int i = 0; i < numRows; i++) {
            vector<int> row;

            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.push_back(1);
                }
                else {
                    row.push_back(triangle[j - 1] + triangle[j]);
                }
            }

            result.push_back(row);
            triangle = row;
        }

        return result;
    }
};
