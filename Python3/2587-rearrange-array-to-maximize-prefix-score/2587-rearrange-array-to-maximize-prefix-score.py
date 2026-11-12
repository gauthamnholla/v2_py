from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = 0
        for i, x in enumerate(nums):
            total += x
            if total <= 0:
                return i
        return len(nums)