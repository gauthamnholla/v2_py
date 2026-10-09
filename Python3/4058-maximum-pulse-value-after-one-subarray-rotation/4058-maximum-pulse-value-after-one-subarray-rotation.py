class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        S = [0] * n
        S[0] = nums[0]
        
        for i in range(1, n):
            S[i] = S[i-1] + (nums[i] if i % 2 == 0 else -nums[i])
            
        original_pulse = S[n-1]
        max_delta = 0
        
        min_even = float('inf')
        min_odd = float('inf')
        
        for l in range(n - 1, -1, -1):
            min_same = min_even if l % 2 == 0 else min_odd
            min_diff = min_odd if l % 2 == 0 else min_even
            
            if min_same != float('inf'):
                delta1 = -2 * (min_same - S[l])
                if delta1 > max_delta:
                    max_delta = delta1
                    
            if min_diff != float('inf'):
                prev_S = 0 if l == 0 else S[l-1]
                delta2 = -2 * (min_diff - prev_S)
                if delta2 > max_delta:
                    max_delta = delta2
                    
            if l % 2 == 0:
                min_even = min(min_even, S[l])
            else:
                min_odd = min(min_odd, S[l])
                
        return original_pulse + max_delta
        
  