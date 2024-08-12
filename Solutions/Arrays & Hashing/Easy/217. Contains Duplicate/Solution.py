# 217. Contains Duplicate (Easy)

# Topics: Array, HashTable, Sorting

# Question: Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.

# Time Complexity: O(n) - We iterate through the list once to insert elements
# into the set.
# Space Complexity: O(n) - The space used by the set is proportional to the
# number of unique elements.

# Time Spent: 00:03:12

# My Solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        if len(test) != len(nums):
            return True
        return False


# Time Complexity: O(n) - (Same reason as above)
# Space Complexity: O(n) - (Same reason as above)

# NeetCode Solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False