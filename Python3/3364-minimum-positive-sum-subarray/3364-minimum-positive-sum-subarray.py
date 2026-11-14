from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        best = float("inf")
        for size in range(l, r + 1):
            for start in range(n - size + 1):
                s = pre[start + size] - pre[start]
                if 0 < s < best:
                    best = s

        return best if best != float("inf") else -1