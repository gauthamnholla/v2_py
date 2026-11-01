from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)

        # For each hat, which people like it
        likes = [[] for _ in range(41)]
        for person, prefs in enumerate(hats):
            for h in prefs:
                likes[h].append(person)

        full = (1 << n) - 1
        dp = [0] * (1 << n)
        dp[0] = 1  # nobody has a hat yet

        for h in range(1, 41):
            if not likes[h]:
                continue
            # Go from high masks to low so each hat is given to at most one person
            for mask in range(full, -1, -1):
                if dp[mask] == 0:
                    continue
                for p in likes[h]:
                    if not mask & (1 << p):
                        nxt = mask | (1 << p)
                        dp[nxt] = (dp[nxt] + dp[mask]) % MOD

        return dp[full]