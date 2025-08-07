# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union = UnionFind(nums)
        for num in nums:
            if num - 1 in union.parent:
                union.union(num, num - 1)

        if len(union.size.values()) == 0:
            return 0
        return max(union.size.values())
