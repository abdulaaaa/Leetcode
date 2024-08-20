# 128. Longest Consecutive Sequence (Medium) (Not Finished)

# Topics: Array, Hash Table, Union Find

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:10:44

# Trouble I had:
# The approach I had for this problem was to implement a counting sort which is
# O(n) time and then just counting the consecutive numbers from there onwards.


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - the set stores unique values from the list

# NeetCode Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #neetcode solution
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if it is the start of the sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest