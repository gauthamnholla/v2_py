from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        LIMIT = 2520 * 10   # lcm(1..10) * max possible gcd
        n = len(nums)
        best = 0

        for i in range(n):
            prod, g, l = 1, 0, 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod > LIMIT:
                    break           # the product only grows from here, so no match is possible
                if prod == l * g:
                    best = max(best, j - i + 1)

        return best