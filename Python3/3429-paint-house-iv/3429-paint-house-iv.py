from typing import List

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        INF = float("inf")
        pairs = [(a, b) for a in range(3) for b in range(3) if a != b]

        # dp[(a, b)] = min cost so far, with the left house of the latest pair colored a
        # and its mirror house on the right colored b
        dp = {(a, b): cost[0][a] + cost[n - 1][b] for a, b in pairs}

        for i in range(1, n // 2):
            j = n - 1 - i
            new = {}
            for a, b in pairs:
                best = INF
                for (pa, pb), val in dp.items():
                    if pa != a and pb != b:   # neighbors on each side differ
                        best = min(best, val)
                new[(a, b)] = best + cost[i][a] + cost[j][b]
            dp = new

        return min(dp.values())