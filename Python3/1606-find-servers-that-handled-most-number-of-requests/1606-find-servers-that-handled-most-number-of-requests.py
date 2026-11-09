import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # free: keys arranged so the smallest key is the next free server at or after i % k
        free = list(range(k))
        busy = []            # (finish time, server id)
        handled = [0] * k

        for i, (t, d) in enumerate(zip(arrival, load)):
            # Release servers that are done; re-key them relative to request i
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                heapq.heappush(free, i + (s - i) % k)
            if not free:
                continue                      # all busy: drop the request
            s = heapq.heappop(free) % k
            handled[s] += 1
            heapq.heappush(busy, (t + d, s))

        top = max(handled)
        return [s for s in range(k) if handled[s] == top]