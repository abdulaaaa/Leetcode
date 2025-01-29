class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # neetcode solution
        l, r = 0, 0

        while r < len(nums):
            count = 1
            # we do r + 1 < len(nums) so it doesn't go out of bounds
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            # it should save at most 2
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
