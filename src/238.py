# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        length = len(nums)
        prefix_arr = [0] * length
        postfix_arr = [0] * length
        for i in range(length):
            prefix *= nums[i]
            prefix_arr[i] = prefix
            postfix *= nums[length - 1 - i]
            postfix_arr[length - 1 - i] = postfix

        for i in range(length):
            nums[i] = 1
            if i - 1 >= 0:
                nums[i] *= prefix_arr[i-1]
            if i + 1 <= length - 1:
                nums[i] *= postfix_arr[i+1]
        return nums


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        length = len(nums)
        out = [1] * length
        for i in range(length):
            out[i] *= prefix
            prefix *= nums[i]
            out[length - 1 - i] *= postfix
            postfix *= nums[length - 1 - i]
        return out
