from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda e: e[1])
        cnt = [0] * (n + 1)   # requests per server inside the window
        active = 0            # servers with at least one request in the window
        ans = [0] * len(queries)
        left = right = 0

        for qi in sorted(range(len(queries)), key=lambda i: queries[i]):
            q = queries[qi]
            # Add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                right += 1
            # Remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active

        return ans