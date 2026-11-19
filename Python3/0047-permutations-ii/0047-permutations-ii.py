from collections import Counter
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        n = len(nums)
        result = []
        path = []

        def backtrack():
            if len(path) == n:
                result.append(path[:])
                return
            for x in counts:
                if counts[x] > 0:
                    counts[x] -= 1
                    path.append(x)
                    backtrack()
                    path.pop()
                    counts[x] += 1

        backtrack()
        return result