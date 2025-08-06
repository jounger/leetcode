# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            b = target - num
            if b not in hashmap:
                hashmap[num] = i
                continue
            return [i, hashmap.get(b, 0)]
        return []
