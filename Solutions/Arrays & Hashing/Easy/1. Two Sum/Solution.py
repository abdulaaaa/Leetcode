# 1. Two Sum (Easy)

# Topics: Array, Hash Table

# Question: Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.

# Time Complexity: O(n) - You have to loop through the enumerated nums

# Space Complexity: O(n) - Stores key value pairs for each value in the nums

# Time Spent: 00:07:36

# My Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {} # num : index

        for i,n in enumerate(nums):
            complacent = target - n

            if complacent in values:
                return [values[complacent],i]
            values[n] = i


# Time Complexity: O(n) - (Same as above)

# Space Complexity: O(n) - (Same as above)

# NeetCode Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i,n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return
