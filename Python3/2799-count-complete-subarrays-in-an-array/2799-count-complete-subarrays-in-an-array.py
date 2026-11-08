from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))          # distinct values in the whole array
        cnt = defaultdict(int)
        left = 0
        ans = 0

        for x in nums:
            cnt[x] += 1
            # Shrink while the window still contains all k distinct values
            while len(cnt) == k:
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                left += 1
            ans += left             # starts 0..left-1 all give complete subarrays
        return ans