class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # Start a new subarray with just the current element
            new_dp[num_mod] += 1
            
            # Extend all previous subarrays ending at the prior position
            for r in range(k):
                if dp[r] > 0:
                    new_mod = (r * num_mod) % k
                    new_dp[new_mod] += dp[r]
            
            # Accumulate the counts into the global result
            for r in range(k):
                result[r] += new_dp[r]
                
            dp = new_dp
            
        return result
        