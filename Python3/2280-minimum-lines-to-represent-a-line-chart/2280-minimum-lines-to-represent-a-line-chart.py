from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        pts = sorted(stockPrices)
        n = len(pts)
        if n == 1:
            return 0

        lines = 1
        for i in range(2, n):
            x0, y0 = pts[i - 2]
            x1, y1 = pts[i - 1]
            x2, y2 = pts[i]
            # Same slope  <=>  (y1 - y0) / (x1 - x0) == (y2 - y1) / (x2 - x1)
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
                lines += 1

        return lines