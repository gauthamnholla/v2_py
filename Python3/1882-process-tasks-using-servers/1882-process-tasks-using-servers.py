import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (time it becomes free, weight, index)
        ans = [0] * len(tasks)
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)                 # task j can't start before it arrives
            if not free:
                t = max(t, busy[0][0])    # wait for the next server to finish
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans[j] = i
            heapq.heappush(busy, (t + dur, w, i))

        return ans