class Solution(object):
    def largestInteger(self, nums, k):
        f = [0] * 51
        max_freq = -1 
        for num in nums:
            f[num] += 1
        for i in range(len(nums)):
            if (
                k == len(nums) or (f[nums[i]] == 1 and 
                (
                    k == 1
                    or i == 0
                    or i == len(nums) - 1
                ))
            ):
                max_freq = max(nums[i], max_freq)
        return max_freq

