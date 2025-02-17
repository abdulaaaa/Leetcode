class RevisedSolution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # the answer is at least 1
        l = 1

        for r in range(1, len(nums)):
            # we got to a unique value
            if nums[r] != nums[r - 1]:
                # since it is in place set it at position l
                nums[l] = nums[r]
                l += 1
        return l
    
    # time complexity: O(n)
    # space complexity; O(1)
