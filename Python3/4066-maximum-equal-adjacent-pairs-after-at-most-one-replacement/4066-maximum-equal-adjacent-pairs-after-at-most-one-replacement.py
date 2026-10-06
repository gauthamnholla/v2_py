class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = sum(a == b for a, b in pairwise(nums))
        gain = Counter((min(a, b), max(a, b)) for a, b in pairwise(nums) if a != b)
        return base + max(gain.values(), default=0)