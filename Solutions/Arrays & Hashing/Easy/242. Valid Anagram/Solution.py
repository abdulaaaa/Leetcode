# 242. Valid Anagram (Easy)

# Topics: HashTable, String, Sorting

# Question: Given two strings s and t, return true if t is an anagram of s,
# and false otherwise

# Time Complexity: O(n log n) - Sorting the strings takes O(n log n) time,
# where n is the length of the strings.

# Space Complexity: O(1) - No extra space is used other than for sorting the
# strings. The space complexity is constant if we disregard the space used by
# the sorting algorithm.

# Time Spent: 00:02:15

# My Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


# Time Complexity: O(n) - The for loop that counts the characters in s and t
# runs in O(n) time, where n is the length of the strings. Comparing the counts
# in the two dictionaries also takes O(n) time in the worst case. Thus, the
# overall time complexity is O(n)

# Space Complexity: O(n) - The space used by the countS and countT dictionaries
# is proportional to the number of unique characters in the strings. In the
# worst case, if all characters are unique, the space complexity is O(n), where
# n is the length of the strings.

# NeetCode Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True