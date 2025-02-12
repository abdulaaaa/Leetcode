class Solution:
    def jump(self, nums: List[int]) -> int:
        # neetcode solution
        res = 0

        l = r = 0 # setting up two pointers for the range

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1): # making r index inclusive
                farthest = max(farthest, i + nums[i]) # finding the farthest point in the range
            l = r + 1
            r = farthest
            res += 1
        return res
