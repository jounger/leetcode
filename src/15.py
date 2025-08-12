# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = set()
        i = 0
        while i < len(nums) - 1:
            num = nums[i]
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum3 = num + nums[j] + nums[k]
                if sum3 >= 0:
                    if sum3 == 0:
                        out.add((num, nums[j], nums[k]))
                    if j == k - 1 and i == j - 1:
                        break
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    if k < 0:
                        break
                    continue
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
        return list(out)
