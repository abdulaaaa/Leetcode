# 20. Valid Parentheses (Easy) (Not Finished)

# Topics: String, Stack

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:17:02

# My Solution:
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
# Trouble I had:
# The plan I had for this problem was to add each of the opening brackets into
# and see if the closeset corresponding closing bracket comes next. Even though
# I had a close enough Idea I didn't know to implement it well. I need to go
# back to pen and paper when solving such questions.


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - we store the values in a stack.

# NeetCode Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        #neetcode solution

        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            #check if the character is one of the closing brackets
            if c in closeToOpen:
                # if it isn't empty and the last value is its representing
                # opening bracket then pop.
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

