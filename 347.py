# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import Any, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap: dict[int, int] = dict()
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        sorted_by_value = dict(
            sorted(hashmap.items(), key=lambda item: -item[1]))
        keys = list(sorted_by_value.keys())
        return keys[0:k]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        hashmap: dict[int, int] = dict()
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        arr: List[Any] = [None] * (len(nums) + 1)
        for key, value in hashmap.items():
            if arr[value] == None:
                arr[value] = []
            arr[value].append(key)

        out = []
        for i in range(len(arr) - 1, -1, -1):
            sub_arr = arr[i]
            if sub_arr == None:
                continue
            for item in sub_arr:
                out.append(item)
                if len(out) == k:
                    return out
        return out[0: k]
