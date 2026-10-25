from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float("inf")

        for row in matrix:
            for x in row:
                if x < 0:
                    neg_count += 1
                ax = abs(x)
                total += ax
                min_abs = min(min_abs, ax)

        if neg_count % 2 == 0:
            return total
        return total - 2 * min_abs