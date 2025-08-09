# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            s = len(stack) - 1
            while s >= 0:
                if temp <= stack[s][0]:
                    break
                out[stack[s][1]] = i - stack[s][1]
                stack.pop(s)
                s = len(stack) - 1
            stack.append((temp, i))
        return out
