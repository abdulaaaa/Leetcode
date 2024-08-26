# 3. Longest Substring Without Repeating Characters (Medium) (Not Finished)

# Topics: Hash Table, String, Sliding Window

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:16:10

# My Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        values = set()
        values.add(s[0])

        values_size = 1

        max_value_size = 1

        l,r = 0, 1

        while r < len(s):
            if s[r] not in values:
                values.add(s[r])
                values_size += 1
                max_value_size = max(max_value_size, values_size)
            else:
                l += 1
                values_size = 1
                values.clear()
                values.add(s[l])
            r += 1

        return max_value_size
# Trouble I had:
# The plan I had for this problem was to add each of the unique substring to set
# and then find the largest possible length for a unique set. If a repeating
# character would ocurr, it would then also reset the set but also keep track of
# the largest size. My code does pass for some test cases but also fails on test
# cases such as "dvdf" as is return 2 instead of 3


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - we store the value in a set.

# NeetCode Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # used to store unique values
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # will check if the value in the right ptr is the duplicate
            # if so it will continue removing from the left until the
            # first value of the duplicate is gone.
            # then we would save the size of that substring
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

