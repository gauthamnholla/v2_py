import math
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        r2 = radius * radius
        best = [0, 0]
        best_q = 0

        for x in range(51):
            for y in range(51):
                q = 0
                for tx, ty, tq in towers:
                    d2 = (tx - x) ** 2 + (ty - y) ** 2
                    if d2 <= r2:  # reachable
                        q += int(tq / (1 + math.sqrt(d2)))
                if q > best_q:  # strict ">" keeps the lexicographically smallest
                    best_q = q
                    best = [x, y]

        return best