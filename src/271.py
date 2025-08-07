# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/description/

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_strs = []
        for s in strs:
            encode_s = []
            if len(s) == 0:
                encode_s.append("e")
            for c in s:
                encode_s.append(f"{ord(c)}")
            encode_strs.append(f"c".join(encode_s))
        return f"w".join(encode_strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        if len(s) == 0:
            return strs

        ss = s.split("w")
        for w in ss:
            chars = w.split("c")
            for i, c in enumerate(chars):
                if c == "e":
                    chars[i] = ""
                else:
                    chars[i] = chr(int(c))
            strs.append("".join(chars))
        return strs
