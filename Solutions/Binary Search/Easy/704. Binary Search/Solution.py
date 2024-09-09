# 1. Binary Search (Easy)

# Topics: Array, Binary Search

# Time Complexity: O(n) - You loop through the values in a linear fashion

# Space Complexity: O(1) - No extra data structure is being used to store data

# Time Spent: 00:05:56

# My Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


# Time Complexity: O(n) - (Same as above)

# Space Complexity: O(1) - (Same as above)

# NeetCode Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1


        while l <= r:
            # we wan't to do calculate the mid in this way because in other
            # languages this might cause an overflow
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
