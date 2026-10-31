from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        h, w = stampHeight, stampWidth

        # pre[i][j] = number of occupied cells in grid[0..i-1][0..j-1]
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row, cur, nxt = grid[i], pre[i], pre[i + 1]
            for j in range(n):
                nxt[j + 1] = row[j] + cur[j + 1] + nxt[j] - cur[j]

        # Place a stamp at every top-left corner where it fits on empty cells only
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m - h + 1):
            for j in range(n - w + 1):
                r2, c2 = i + h, j + w
                if pre[r2][c2] - pre[i][c2] - pre[r2][j] + pre[i][j] == 0:
                    diff[i][j] += 1
                    diff[i][c2] -= 1
                    diff[r2][j] -= 1
                    diff[r2][c2] += 1

        # Prefix-sum the difference array to get coverage; check every empty cell
        cov = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cov[i + 1][j + 1] = diff[i][j] + cov[i][j + 1] + cov[i + 1][j] - cov[i][j]
                if grid[i][j] == 0 and cov[i + 1][j + 1] == 0:
                    return False
        return True