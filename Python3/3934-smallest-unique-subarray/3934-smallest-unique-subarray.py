class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        BASE = 911382323
        MOD = 10**9 + 7

        # large random base to represent number
        # similar to:
        # 1234 = 1*10^3 + 2*10^2 + 3*10 + 4
        # hash = a*BASE^3 + b*BASE^2 + c*BASE + d

        power = [1] * (n + 1)
        # to store powers of base

        pref = [0] * (n + 1)
        # pref[i] stores hash of first i elements

        for i in range(n):
            power[i + 1] = (power[i] * BASE) % MOD
            pref[i + 1] = (pref[i] * BASE + nums[i] + 1) % MOD

        # gives hash of subarray l to r
        def getHash(l, r):

            return (
                pref[r + 1]
                - (pref[l] * power[r - l + 1]) % MOD
                + MOD
            ) % MOD

        # checks if unique subarray of length exists
        def possible(length):

            freq = {}

            # generate all subarray hashes
            for i in range(n - length + 1):

                h = getHash(i, i + length - 1)

                freq[h] = freq.get(h, 0) + 1

            # check whether any hash appears once
            for cnt in freq.values():

                if cnt == 1:
                    return True

            return False

        low = 1
        high = n

        ans = n

        while low <= high:

            mid = low + (high - low) // 2

            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans