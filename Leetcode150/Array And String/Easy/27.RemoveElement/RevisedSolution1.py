class RevisedSolution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            # we just have to move the numbers that aren't val
            # up to the front, it doesn't matter what the end is.
            # and return k which the amount we move to the front.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        # Time Complexity: O(n)
        # Space Complexity: O(1)