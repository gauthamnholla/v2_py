from collections import defaultdict
from typing import List

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        seen[0] = 1          # empty prefix
        prefix = 0
        ans = 0
        for x in nums:
            prefix ^= x
            ans += seen[prefix]   # earlier prefixes equal to this one
            seen[prefix] += 1
        return ans