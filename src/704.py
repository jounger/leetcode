# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
