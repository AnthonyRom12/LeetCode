"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)  # create a dict, where keys will be sorted letters of the each words, and values will be lists of the words with the same letters
        for word in strs:
            sorted_word = ''.join(sorted(word))  # sort letters in each words and convert to string
            anagram_dict[sorted_word].append(word)  # Add a word to the list of the corresponding set of letters
        result = list(anagram_dict.values())
        return result  # Return a list of all anagram groups
