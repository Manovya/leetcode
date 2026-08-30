class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            self.rob_linear(nums, 0, n - 2),
            self.rob_linear(nums, 1, n - 1)
        )

    def rob_linear(self, nums: List[int], st: int, end: int) -> int:

        n = end - st + 1

        dp = [0] * n

        dp[0] = nums[st]

        if n > 1:
            dp[1] = max(nums[st], nums[st + 1])

        j = 2

        for i in range(st + 2, end + 1):
            dp[j] = max(dp[j - 2] + nums[i], dp[j - 1])
            j += 1

        return dp[n - 1]