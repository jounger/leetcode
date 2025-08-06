# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap: dict[str, List[str]] = dict()
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in hashmap:
                hashmap[sorted_str] = []
            hashmap[sorted_str].append(s)
        return list(hashmap.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = 97
        alphabet_count = 26
        az = {chr(i): i for i in range(a, a + alphabet_count)}

        hashmap: dict[tuple, list[str]] = dict()
        for s in strs:
            arr = [0] * alphabet_count
            for c in s:
                position = az[c] - az['a']
                arr[position] += 1
            key = tuple(arr)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())
