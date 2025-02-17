class Solution:
    def trap(self, height: List[int]) -> int:
        # neetcode solution

        # this is if there is no barriers in the first place
        if not height: return 0

        # set our right and left pointers
        left, right = 0, len(height) - 1
        # we need to set the max for left and right
        leftMax, rightMax = height[left], height[right]
        res = 0
        # traverse through all points
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])

                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])

                res += rightMax - height[right]
        return res

