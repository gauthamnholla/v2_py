from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = ["." * n]                      # top row: all free
        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")  # only the last column is free
        return grid