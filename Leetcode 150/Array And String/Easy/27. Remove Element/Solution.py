class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # This right here was my initial approach but popping a value and iterating a list causes
        # issues with indexing

        # k = len(nums)

        # for val in nums:
        #     nums.pop(val)
        #     k -= 1
        # return k


        # neetcode solution

        k = 0  # Pointer for the new position of valid elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Copy non-`val` elements to the front
                k += 1

        return k


