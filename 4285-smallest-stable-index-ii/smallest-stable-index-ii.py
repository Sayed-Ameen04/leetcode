class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # right[i] = minimum element from index i to n - 1
        right = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        # Maximum element from index 0 to i
        left = nums[0]

        for i, x in enumerate(nums):
            left = max(left, x)

            if left - right[i] <= k:
                return i

        return -1