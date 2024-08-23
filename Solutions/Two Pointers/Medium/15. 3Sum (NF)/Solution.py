# 15. 3Sum (Medium) (Not Finished)

# Topics: Array, Two Pointers, Sorting

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:24:56

# My Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        print(nums)

        final_list = []

        for i in range(len(nums)):
            complacent = -1 * nums[i]

            left = 1
            right = len(nums) - 1

            while left < right:
                value = nums[left] + nums[right]
                if value < complacent:
                    left += 1
                elif value > complacent:
                    right -= 1
                elif value == complacent:
                    print([nums[i],nums[left],nums[right]])
                else:
                    left += 1
                    right -= 1
# Trouble I had:
# The plan I had for this problem was to first sort the entire list and in a
# linear fashion make each value basically the negative target. Then I would
# two sum 2 solution.


# Time Complexity: O(n^2) - Due to the nested loop with the for and while

# Space Complexity: O(1) - No extra space is being used except for the return
# value

# NeetCode Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # neetcode solution
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # If the previous value is the same we should continue to the next
            # value.
            if i > 0 and a == nums[i - 1]:
                continue

            # This is just continuation of 2Sum

            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # increment the left pointer and if the value is the same
                    # increment it again. (but neetcode had the good idea to
                    # check l < r)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res