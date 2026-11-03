from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(m - x for x in nums)