class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        st = 0
        end = len(nums) - 1

        while st < end:
            mid = st + (end - st) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is correct, single element is on the right
                st = mid + 2
            else:
                # Pair is broken, single element is on the left
                end = mid

        return nums[st]