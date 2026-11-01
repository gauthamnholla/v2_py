from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {a for a, _ in paths}
        for _, b in paths:
            if b not in starts:
                return b
        return ""