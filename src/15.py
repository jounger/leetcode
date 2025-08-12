# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = set()
        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum3 = num + nums[j] + nums[k]
                if sum3 == 0:
                    out.add((num, nums[j], nums[k]))
                if j == k - 1 and i == j - 1:
                    break
                if sum3 > 0:
                    k -= 1
                else:
                    j += 1
        return list(out)
