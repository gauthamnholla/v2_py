class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n, total = len(nums), sum(nums) % k
        doubled = [2 * x % k for x in nums]
        if total == 0 or total in doubled:  # whole array works
            return n

        prefix = [s % k for s in accumulate(nums, initial=0)]
        last = [-1] * k
        for i, c in enumerate(prefix):
            last[c] = i
        last += last  # last[c + v] == last[(c + v) % k]

        nxt, after = [n] * k, [n] * n  # nxt[v]: first index >= start with this v
        for i, v in zip(range(n - 1, -1, -1), reversed(doubled)):
            after[i], nxt[v] = nxt[v], i  # after[i]: next index with the same v
        values = [v for v in range(k) if nxt[v] < n]

        best, seen = 0, set()
        for start, (c, d) in enumerate(zip(prefix, doubled)):
            if n - start <= best:
                break
            if c not in seen:  # first[c] == start
                seen.add(c)
                ends = [last[c + v] for v in values]
                fits = map(lt, map(nxt.__getitem__, values), ends)
                best = max(best, last[c] - start, max(compress(ends, fits), default=0) - start)
            nxt[d] = after[start]  # index start leaves the window
        return best