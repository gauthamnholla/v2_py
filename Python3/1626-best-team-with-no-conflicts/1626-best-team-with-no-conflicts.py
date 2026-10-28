from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))  # by age, then score
        n = len(players)
        dp = [0] * n  # dp[i] = best team score where player i is the last one picked

        for i in range(n):
            s_i = players[i][1]
            dp[i] = s_i
            for j in range(i):
                if players[j][1] <= s_i:
                    dp[i] = max(dp[i], dp[j] + s_i)

        return max(dp)