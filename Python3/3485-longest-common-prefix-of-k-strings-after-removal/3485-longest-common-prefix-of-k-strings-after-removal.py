from collections import deque
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        if n - 1 < k:
            return [0] * n

        order = sorted(range(n), key=lambda i: words[i])
        s = [words[i] for i in order]

        def lcp(a: str, b: str) -> int:
            m = min(len(a), len(b))
            i = 0
            while i < m and a[i] == b[i]:
                i += 1
            return i

        # w[j]: best prefix for the k sorted words s[j..j+k-1]
        w = [lcp(s[j], s[j + k - 1]) for j in range(n - k + 1)]
        # v[j]: best prefix for s[j..j+k] with one middle word removed
        v = [lcp(s[j], s[j + k]) for j in range(n - k)]

        pre = w[:]
        for j in range(1, len(pre)):
            pre[j] = max(pre[j], pre[j - 1])
        suf = w[:]
        for j in range(len(suf) - 2, -1, -1):
            suf[j] = max(suf[j], suf[j + 1])

        res = [0] * n
        dq = deque()  # sliding-window max over v[j] for j in [i-k+1, i-1]
        nxt = 0
        for i in range(n):
            best = 0
            if i - k >= 0:                  # windows entirely before i
                best = pre[i - k]
            if i + 1 <= n - k:              # windows entirely after i
                best = max(best, suf[i + 1])

            # windows that had i in the middle, with i removed
            hi = min(i - 1, n - k - 1)
            while nxt <= hi:
                while dq and v[dq[-1]] <= v[nxt]:
                    dq.pop()
                dq.append(nxt)
                nxt += 1
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            if dq:
                best = max(best, v[dq[0]])

            res[order[i]] = best
        return res