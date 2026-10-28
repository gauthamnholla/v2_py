from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [set() for _ in range(n)]  # reachable XOR values in the row above

        for i in range(m):
            cur = [set() for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    cur[j] = {v}
                    continue
                reach = set()
                if i > 0:
                    reach |= prev[j]       # coming from above
                if j > 0:
                    reach |= cur[j - 1]    # coming from the left
                cur[j] = {x ^ v for x in reach}
            prev = cur

        return min(prev[n - 1])