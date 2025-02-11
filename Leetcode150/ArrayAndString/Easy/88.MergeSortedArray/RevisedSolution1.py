class RevisedSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # this gets the last index in nums1
        last = m + n - 1

        # this will place the values towards the end of nums1
        # we didn't create a new array so we can save on
        # space complexity
        while (m > 0 and n > 0):
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill in the rest, this would be done if we looped through nums1 and
        # now we need to continue looping through nums2. keep in mind
        # we dont need to do a check becuase nums2 array is already sorted
        while (n > 0):
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1

        # time complexity: O(n)
        # space complexity: O(1)