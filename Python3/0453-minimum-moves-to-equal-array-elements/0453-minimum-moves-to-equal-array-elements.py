from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum(nums) - m * len(nums)