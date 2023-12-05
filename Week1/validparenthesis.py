#Link -> https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(":")","{":"}","[":"]"}
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if not stack or brackets[stack[-1]] != p:
                    return False
                else:
                    stack.pop()
        
        return not stack
        