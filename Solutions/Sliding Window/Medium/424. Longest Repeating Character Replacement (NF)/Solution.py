# 424. Longest Repeating Character Replacement (Medium) (Not Finished)

# Topics: Hash Table, String, Sliding Window

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:00:00

# Trouble I had:
# I genuinely don't know how to solve this question, this question was
# definately a harder medium. After looking at neetcodes solution the idea is
# to the get the sliding window substring and replace the characters that ocurr
# the least amount of times as long as it is below k. This would be a valid
# answer and your goal is to find the largest substring for that.


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - we store the value in a hashmap.

# NeetCode Solution:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            # store the amount of characters in a hashmap
            count[s[r]] = 1 + count.get(s[r],0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res