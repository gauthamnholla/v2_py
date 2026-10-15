class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        or_cache = [0] * len(nums)
        
        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return abs(nums[left] - k)
            
            mid = left + (right - left) // 2
            left_result = divide_and_conquer(left, mid)
            right_result = divide_and_conquer(mid + 1, right)
            
            combined_or = nums[mid] | nums[mid + 1]
            current_min_diff = min(abs(combined_or - k), left_result, right_result)
            
            # Early stopping condition
            if combined_or >= k:
                return current_min_diff
            
            or_cache[mid] = combined_or
            or_cache[mid + 1] = combined_or
            
            left_bound = left
            # Calculate leftmost index where the OR value with nums[mid+1] is less than k
            for i in range(mid - 1, left - 1, -1):
                or_cache[i] = or_cache[i + 1] | nums[i]
                current_min_diff = min(current_min_diff, abs(or_cache[i] - k))
                # Early stopping condition
                if or_cache[i] >= k:
                    left_bound = i + 1
                    break
            
            # Sliding window to find the minimum difference
            for right_bound in range(mid + 1, right + 1):
                or_cache[right_bound] = or_cache[right_bound - 1] | nums[right_bound]
                combined_or = or_cache[left_bound] | or_cache[right_bound]
                current_min_diff = min(current_min_diff, abs(combined_or - k))
                
                while left_bound < mid and combined_or > k:
                    left_bound += 1
                    combined_or = or_cache[left_bound] | or_cache[right_bound]
                    current_min_diff = min(current_min_diff, abs(combined_or - k))
                
                # Early stopping condition
                if current_min_diff == 0 or (left_bound == mid and combined_or > k):
                    return current_min_diff
            
            return current_min_diff
        
        return divide_and_conquer(0, len(nums) - 1)
        