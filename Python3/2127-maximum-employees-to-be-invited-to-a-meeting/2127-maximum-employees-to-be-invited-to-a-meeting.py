from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for f in favorite:
            indeg[f] += 1

        # Peel off people not on a cycle; track the longest chain leading into each person
        chain = [0] * n  # longest chain of people ending just before this person
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u = q.popleft()
            v = favorite[u]
            chain[v] = max(chain[v], chain[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        # Everyone left with indeg > 0 is on a cycle
        biggest_cycle = 0
        pairs_total = 0
        for i in range(n):
            if indeg[i] == 0:
                continue
            # Walk the cycle, measuring its length and marking it done
            length = 0
            j = i
            while indeg[j]:
                indeg[j] = 0
                length += 1
                j = favorite[j]
            if length == 2:
                pairs_total += 2 + chain[i] + chain[favorite[i]]
            else:
                biggest_cycle = max(biggest_cycle, length)

        return max(biggest_cycle, pairs_total)