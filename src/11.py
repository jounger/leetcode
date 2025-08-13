# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            min_height = min(height[i], height[j])
            area = (j - i) * min_height
            if area > maximum:
                maximum = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maximum
