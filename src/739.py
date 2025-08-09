# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

from typing import List


# Time Limit Exceeded 36/48
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            stack.append((temp, i))
            s = len(stack) - 1
            while s >= 0:
                m = temp - stack[s][0]
                if m < 0:
                    break
                if m == 0:
                    s -= 1
                    continue
                p = stack[s][1]
                out[p] = i - p
                stack.pop(s)
                s = len(stack) - 1
        return out
