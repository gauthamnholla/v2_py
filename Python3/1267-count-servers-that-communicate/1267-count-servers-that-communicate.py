from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(r) for r in grid]
        cols = [sum(c) for c in zip(*grid)]
        return sum(
            1
            for i, r in enumerate(grid)
            for j, v in enumerate(r)
            if v and (rows[i] > 1 or cols[j] > 1)
        )