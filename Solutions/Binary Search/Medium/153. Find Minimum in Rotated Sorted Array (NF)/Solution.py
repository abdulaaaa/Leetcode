# 153. Find Minimum in Rotated Sorted Array (Medium) (Not Finished)

# Topics: Array Binary Search

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:21:02

# My Solution:
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1


        while l < r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            elif: nums[m] < nums[m - 1]:
                return nums[m]
            elif:
# Trouble I had:
# I think I might be brain dead when trying to solve this question. It is very
# straight forward but taking into consideration of edge cases is something I
# am not doing. I also have no Idea on how to approach this question in the
# right manner


# Time Complexity: O(logn) - we use binary search

# Space Complexity: O(1) - we dont store the values anywhere

# NeetCode Solution:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

