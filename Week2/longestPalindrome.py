# Link - https://leetcode.com/problems/longest-palindrome/description/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = set()
        for char in s:
            try:
                memo.remove(char)
            except KeyError:
                memo.add(char)
        
        has_odd_number = len(memo) > 0
        return len(s) - len(memo) + 1 if has_odd_number else len(s)
        