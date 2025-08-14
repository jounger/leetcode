# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = (m * n) - 1
        while i <= j:
            mid = (i + j) // 2
            real_m = mid // n
            real_n = mid % n
            v = matrix[real_m][real_n]
            if v == target:
                return True
            if v > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
