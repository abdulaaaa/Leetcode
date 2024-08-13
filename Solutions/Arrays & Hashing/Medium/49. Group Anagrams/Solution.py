# 49. Group Anagrams (Medium)

# Topics: Array, Hash Table, String, Sorting

# Question: Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.

# Time Complexity: O(n logn) - this is a rough estimate the actual answer is way
# longer

# Space Complexity: O(n) - Stores key value pairs

# Time Spent: 00:23:20

# My Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        values = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in values:
                values[sorted_word] = []
            values[sorted_word].append(word)

        sorted_keys = sorted(values.keys())
        final_values = []
        for key in sorted_keys:
            final_values.append(values[key])

        return final_values



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
