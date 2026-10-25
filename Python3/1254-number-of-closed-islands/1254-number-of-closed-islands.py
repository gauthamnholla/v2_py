from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    continue

                # Explore this whole island, marking cells as visited (set to 1)
                closed = True
                stack = [(r, c)]
                grid[r][c] = 1

                while stack:
                    i, j = stack.pop()
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        closed = False  # touches the border
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 0:
                            grid[ni][nj] = 1
                            stack.append((ni, nj))

                if closed:
                    count += 1

        return count