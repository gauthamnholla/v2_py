class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = defaultdict(lambda: [0] * (k + 1))
        best = [0] * (k + 1)
        value = [None] * (k + 1)
        second = [0] * (k + 1)
        second_value = [None] * (k + 1)
        ans = 0
        for x in nums:
            for j in range(k + 1):
                cur = dp[x][j] + 1
                if j > 0:
                    if value[j - 1] != x:
                        cur = max(cur, best[j - 1] + 1)
                    else:
                        cur = max(cur, second[j - 1] + 1)
                dp[x][j] = max(dp[x][j], cur)

            for j in range(k + 1):
                cur = dp[x][j]
                if value[j] == x:
                    best[j] = max(best[j], cur)
                elif cur > best[j]:
                    second[j] = best[j]
                    second_value[j] = value[j]
                    best[j] = cur
                    value[j] = x
                elif cur > second[j]:
                    second[j] = cur
                    second_value[j] = x
                ans = max(ans, cur)
        return ans