# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap: dict[str, int] = dict()
        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
        return not any(hashmap.values())
