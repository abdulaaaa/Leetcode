# 11. Container With Most Water (Medium)

# Topics: Array, Two Pointers, Greedy

# Question: You are given an integer array height of length n. There are n
# vertical lines drawn such that the two endpoints of the ith line are (i, 0)
# and (i, height[i]). Find two lines that together with the x-axis form a
# container, such that the container contains the most water. Return the
# maximum amount of water a container can store.

# Time Complexity: O(n) - We are searching the list forward and backward in
# linear fashion

# Space Complexity: O(1) - no extra data structure is being used to store values

# Time Spent: 00:15:20

# My Solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        min_value = min(height[left], height[right])
        max_area = (right - left) * min_value

        print(max_area)


        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            min_value = min(height[left], height[right])
            max_value = (right - left) * min_value
            max_area = max(max_area, max_value)
        return max_area



# NeetCode Solution:
# basically the same