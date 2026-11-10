from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float("inf")] * n
        for j in range(1, n + 1):
            for d in (1, 2, 3):
                i = j - d
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + d * d)
            dp[j] += costs[j - 1]   # costs is 1-indexed in the statement
        return dp[n]