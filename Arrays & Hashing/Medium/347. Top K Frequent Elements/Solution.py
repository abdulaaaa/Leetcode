class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I understand for this questions we should use a bucketsort but I'm not sure how to implement it so I used help from Neetcode

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


