class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],   # change the two smallest
            nums[-3] - nums[0],   # change the two largest
            nums[-2] - nums[1],   # change the smallest and the largest
        )