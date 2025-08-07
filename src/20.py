# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
                continue

            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if c != pairs[bracket]:
                return False
        return len(stack) == 0
