# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int, i: int, j: int) -> int:
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i, num in enumerate(numbers):
            find = target - num
            found = self.search(numbers, find, i + 1, length - 1)
            if found == -1:
                continue
            return [i+1, found+1]
        raise ValueError("Not found")


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(numbers):
            find = target - num
            if find in hashmap:
                return [hashmap[find]+1, i+1]
            if num not in hashmap:
                hashmap[num] = i
        raise ValueError("Not found")
