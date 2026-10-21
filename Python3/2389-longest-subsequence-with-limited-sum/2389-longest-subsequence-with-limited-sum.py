class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        result = []
        for q in queries:
            start, end = 0, len(nums) - 1
            totalEle = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= q:
                    totalEle = mid
                    start = mid + 1
                else:
                    end = mid - 1
            result.append(totalEle + 1 if totalEle != -1 else 0)
        return result