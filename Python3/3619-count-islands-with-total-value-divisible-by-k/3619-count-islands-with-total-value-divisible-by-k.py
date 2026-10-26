from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                # Explore the island, summing values and marking cells visited (set to 0)
                total = grid[r][c]
                grid[r][c] = 0
                stack = [(r, c)]

                while stack:
                    i, j = stack.pop()
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] > 0:
                            total += grid[ni][nj]
                            grid[ni][nj] = 0
                            stack.append((ni, nj))

                if total % k == 0:
                    count += 1

        return count