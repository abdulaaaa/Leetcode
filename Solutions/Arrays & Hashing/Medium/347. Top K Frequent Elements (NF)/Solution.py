# 347. Top K Frequent Elements (Medium) (Not Finished)

# Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue),
# Bucket Sort, Counting, Quickselect

# Time Complexity - None

# Space Complexity - None

# Time Spent: 00:12:11

# My Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        values = {} # value : amount

        for i in range(len(nums)):
            if nums[i] not in values:
                values[nums[i]] = 1
            else:
                values[nums[i]] = 1 + values.get(nums[i], 0)

        values = list(my_dict.values())
# Trouble I had:
# The plan for this problem was for me to store the values in hashmap and have
# the number of occurences as the value pair. Then I would specifically retrieve
# all the values which then I would sort and return the largest value's key k
# amount of times, the problem is this would be O(n^2) time which is slower than
# the expected O(n logn)


# Time Complexity: O(n) - we loop through the given list in linear time

# Space Complexity: O(n) - we store the values in a hashmap and list in linear
# manner.

# NeetCode Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # neetcode solution using bucketsort
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        # creates a hashmap with value : amount
        for n in nums:
            count[n] = 1 + count.get(n,0)

        # freq is a list that stores other list.
        # this uses a bucketsort method since the amount is basically the key
        # and the values in the list are the ones with the amount.
        for n, c in count.items():
            freq[c].append(n)
        res = []

        # loop backwards through freq and add that to res until we get k elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res