# 155. Min Stack (Medium) (Not Finished)

# Topics: Stack, Design

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:02:00

# Trouble I had:
# This is a design question so I had no clue how the python syntax would look.
# In addition, This question definately confused me since the idea of using a
# second stack that would store the minimum value at each method called didn't
# ever come to mind.


# Time Complexity: O(1) - when calling minStack we just get the top value

# Space Complexity: O(n) - we store the value in a stack.

# NeetCode Solution:
class MinStack:
    #neetcode solution

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        # if the minstack isn't empty youd compare the current value with the
        # value at the top of the minstack, or else it would just be the value
        # with the value.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

