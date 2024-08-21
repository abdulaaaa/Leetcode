# 125. Valid Palindrome (Medium)

# Topics: Two Pointers, String

# Question: A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters and
# numbers.

# Time Complexity: O(n) - We check each value once in a linear fashion from both
# ends.

# Space Complexity: O(n) - We store the a new version of the string that is
# manipulated.

# Time Spent: 00:06:04

# My Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()

        left = 0
        right = len(new_str) - 1

        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True



# NeetCode Solution:
# basically the same