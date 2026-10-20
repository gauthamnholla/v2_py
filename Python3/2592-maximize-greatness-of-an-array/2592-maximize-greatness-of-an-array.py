class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        j = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > nums[j]:
                cnt += 1
                j += 1
        return cnt