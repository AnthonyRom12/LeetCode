/**
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
*
*
*
* Example 1:
*
* Input: n = 3
* Output: ["((()))","(()())","(())()","()(())","()()()"]
* Example 2:
*
* Input: n = 1
* Output: ["()"]
*/

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> combinations = new ArrayList<>();
        backtrack(combinations, "", 0, 0, n);
        return combinations;
    }

    private void backtrack(List<String> combinations, String current, int openCount, int closeCount, int max) {
        // Base case: If the current combination has the desired length (2*n),
        // add it to the list of combinations and return.
        if (current.length() == 2 * max) {
            combinations.add(current);
            return;
        }

        // Recursive case: Add an open parenthesis if there are remaining open parentheses.
        if (openCount < max) {
            backtrack(combinations, current + "(", openCount + 1, closeCount, max);
        }

        // Recursive case: Add a close parenthesis if it can be matched to an open parenthesis.
        if (closeCount < openCount) {
            backtrack(combinations, current + ")", openCount, closeCount + 1, max);
        }
    }
}
