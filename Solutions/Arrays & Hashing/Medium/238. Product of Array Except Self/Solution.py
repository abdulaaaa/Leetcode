# 49. Product of Array Except Self (Medium)

# Topics: Array, Prefix Sum

# Question: Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i].
# You must write an algorithm that runs in O(n) time and without using the
# division operation.

# Time Complexity: O(n) - It loops through the nums in linear fashion and stores
# each numbers post_fix and pre_fix values. Based on that, they will do another
# linear search for the product of the post_fix and pref_x number

# Space Complexity: O(n) - Stores the post_fix, pre_fix, and res arrays

# Time Spent: 00:24:11

# My Solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        post_fix = [0] * len(nums)
        pre_fix = [0] * len(nums)

        res = [0] * len(nums)


        pre_fix[0] = nums[0]
        for i in range(1, len(nums)):
            pre_fix[i] = pre_fix[i - 1] * nums[i]

        post_fix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            post_fix[i] = post_fix[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                res[i] = post_fix[i + 1]
            elif i > 0 and i < (len(nums) - 1):
                res[i] = pre_fix[i - 1] * post_fix[i + 1]
            else:
                res[i] = pre_fix[len(nums) - 2]
        return res



# Time Complexity: O(n)

# Space Complexity: O(1) - We can get rid of the pre_fix and post_fix arrays and
# directly do the multiplication in the result array

# NeetCode Solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

