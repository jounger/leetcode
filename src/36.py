# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

from typing import List


class Solution:
    def is_duplicated(self, nums):
        hashset = set()
        for num in nums:
            if num == ".":
                continue
            if num in hashset:
                return True
            hashset.add(num)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        cols = [["." for _ in range(length)] for _ in range(length)]
        boxes = [["." for _ in range(length)] for _ in range(length)]
        for i, row in enumerate(board):
            if self.is_duplicated(row):
                return False
            for j, col in enumerate(row):
                if col == ".":
                    continue
                cols[j][i] = col
                box_x = (j // 3) + (i // 3) * 3
                box_y = (i % 3) * 3 + j % 3
                boxes[box_x][box_y] = col
        for col in cols:
            if self.is_duplicated(col):
                return False
        for box in boxes:
            if self.is_duplicated(box):
                return False
        return True
