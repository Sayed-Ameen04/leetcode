class Solution(object):
    def subarraySum(self, nums, k):
        current_prefix = 0
        count = 0
        freq = {0:1}
        for num in nums:
            current_prefix += num
            previous_prefix = current_prefix - k

            if previous_prefix in freq:
                count += freq[previous_prefix]
            
            freq[current_prefix] = freq.get(current_prefix, 0) + 1

        return count
