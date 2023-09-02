/*
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 */

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s, int left, int right) {
        // Initialize left and right pointers to check for a palindrome
        left = 0;
        right = s.length() - 1;

        // Compare characters at the left and right pointers while moving towards the center
        while (left < right) {
            if (s[left] != s[right]) {
                return false; // Not a palindrome
            }
            left++;
            right--;
        }
        return true; // It's a palindrome
    }

    string longestPalindrome(string s) {
        int n = s.length();
        if (n < 2) {
            return s; // If the string has 0 or 1 character, it's already a palindrome
        }

        int maxLength = 1;
        int start = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                bool isPalindrome = true;

                // Check if s[i:j] is a palindrome
                for (int k = 0; k < (j - i + 1) / 2; k++) {
                    if (s[i + k] != s[j - k]) {
                        isPalindrome = false;
                        break;
                    }
                }

                // If s[i:j] is a palindrome and longer than the current max, update maxLength and start
                if (isPalindrome && (j - i + 1) > maxLength) {
                    maxLength = j - i + 1;
                    start = i;
                }
            }
        }
        // Extract and return the longest palindromic substring
        return s.substr(start, maxLength);
    }
};
