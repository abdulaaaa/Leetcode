# 739. Daily Temperatures (Medium) (Not Finished)

# Topics: String, Stack

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:21:02

# My Solution:
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        for i in range(len(temperatures) - 2):
            val = 0
            iteration = i

            while temperatures[iteration + 1] > temperatures[iteration]:
                val += 1
                iteration += 1
            stack.append(val)
        return stack
# Trouble I had:
# The plan I had for this problem was to add each of the opening brackets into
# and see if the closeset corresponding closing bracket comes next. Even though
# I had a close enough Idea I didn't know to implement it well. I need to go
# back to pen and paper when solving such questions.


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - we store the values in a stack.

# NeetCode Solution:
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize all the result values to 0
        res = [0] * len(temperatures)
        # the stack will store the pair value of the temperature and
        # corresponding index
        stack = [] # pair : [temp, index]

        for i, t in enumerate(temperatures):
            # while the stack isn't empty and if the current value is greater
            # than the top value of the stack then pop it and update the
            # difference of indexes to get there in the result.
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            # or else we just continue appending to the stack
            stack.append([t, i])
        return res

