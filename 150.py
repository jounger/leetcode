# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

from typing import List


class Solution:
    def is_integer(self, s) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_integer(token):
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            match token:
                case "+":
                    stack.append(left + right)
                case "-":
                    stack.append(left - right)
                case "*":
                    stack.append(left * right)
                case "/":
                    stack.append(int(left / right))
        return stack[0]
