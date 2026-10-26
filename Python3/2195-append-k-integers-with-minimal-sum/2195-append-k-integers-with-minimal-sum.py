from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        limit = k
        total = k * (k + 1) // 2  # sum of 1..k

        for x in sorted(set(nums)):
            if x > limit:
                break
            # x is inside our range: drop it and take the next number past the top
            limit += 1
            total += limit - x

        return total