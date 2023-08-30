"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 """

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            def backtrack(combination, open_count, close_count):
            # Base case: If the combination is of the desired length (2 * n)
            # add it to the list of combinations and return
                if len(combination) == 2 * n:
                    combinations.append(combination)
                    return

                # Recursive case: Add an open parenthesis if there are remaining open paretheses.
                if open_count < n:
                    backtrack(combination + "(", open_count + 1, close_count)

                # Recursive case: Add a close parenthesis if it can be matched to an open parethesis.
                if close_count < open_count:
                    backtrack(combination + ")", open_count, close_count + 1)

            combinations = []  # List to store the generated combinations
            backtrack("", 0, 0)  # Start the recursive process with empty combination
            return combinations
