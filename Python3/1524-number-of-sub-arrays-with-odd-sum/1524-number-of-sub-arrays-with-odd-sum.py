from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0   # the empty prefix (sum 0) is even
        prefix = 0
        ans = 0
        for x in arr:
            prefix += x
            if prefix % 2:
                ans += even   # odd - even = odd
                odd += 1
            else:
                ans += odd    # even - odd = odd
                even += 1
        return ans % MOD