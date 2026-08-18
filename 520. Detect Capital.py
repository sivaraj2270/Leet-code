'''Detect Capital

Example 1:

Input: word = "USA"
Output: true'''

#code link : https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
