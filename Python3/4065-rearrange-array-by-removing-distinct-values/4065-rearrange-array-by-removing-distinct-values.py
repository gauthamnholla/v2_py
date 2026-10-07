class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq, ans = Counter(nums), []
        while freq:
            ans += sorted(freq)
            freq -= Counter(freq.keys())
        return ans