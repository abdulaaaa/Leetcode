# 33. Search in Rotated Sorted Array (Medium) (Not Finished)

# Topics: Array, Binary Search

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:22:33

# My Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0

        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
# Trouble I had:
# I am not sure how to solve such a question. I need to review binary search and
# how to make modifications in such scenario. I straight up don't know how to
# answer this


# Time Complexity: O(logn) - we use binary search

# Space Complexity: O(1) - we dont store the values anywhere

# NeetCode Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <=r :
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # left sorted portion
            if nums[l] <= nums[m]:
                # check the right side
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # check the left side
                else:
                    r = m - 1
            # right sorted portion
            else:
                # check the left side
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # check the right side
                else:
                    l = m + 1
        return -1


