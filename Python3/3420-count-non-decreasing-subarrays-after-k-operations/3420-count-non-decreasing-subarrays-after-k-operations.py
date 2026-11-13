from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        blocks = deque()  # [value, count]: running max from l, grouped; front = left side
        cost = 0          # operations needed for window nums[l..r]
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            # Add nums[l] on the left: it raises every block it is larger than
            cnt = 1
            while blocks and blocks[0][0] <= nums[l]:
                v, c = blocks.popleft()
                cost += (nums[l] - v) * c
                cnt += c
            blocks.appendleft([nums[l], cnt])

            # Too expensive: drop elements from the right end
            while cost > k:
                cost -= blocks[-1][0] - nums[r]
                blocks[-1][1] -= 1
                if blocks[-1][1] == 0:
                    blocks.pop()
                r -= 1

            ans += r - l + 1
        return ans