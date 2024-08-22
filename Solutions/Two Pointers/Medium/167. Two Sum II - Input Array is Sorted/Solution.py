# 167. Two Sum II - Input Array is Sorted (Medium)

# Topics: Array, Two Pointers, Binary Search

# Question: Given a 1-indexed array of integers numbers that is already sorted
# in non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length. Return the indices of the two
# numbers, index1 and index2, added by one as an integer array [index1, index2]
# of length 2.

# Time Complexity: O(n) - We are searching the list forward and backward in
# linear fashion

# Space Complexity: O(n) - no extra data structure is being used to store values

# Time Spent: 00:02:50

# My Solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            value = numbers[left] + numbers[right]
            if value < target:
                left += 1
            elif value > target:
                right -= 1
            else:
                return [left + 1, right + 1]



# NeetCode Solution:
# basically the same