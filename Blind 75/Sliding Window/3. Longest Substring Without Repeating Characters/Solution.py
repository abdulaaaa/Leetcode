class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # my idea is to add the characters into a set and the longest sequence in the set,
        # my approach is wrong because when we hit the second w in pwwkew, it doesn't keep track of it when starting the longest sequence.

        # longest = set()

        # res = 0
        # seq = 0
        # for i in range(len(s)):
        #     if s[i] not in longest:
        #         longest.add(s[i])
        #         seq += 1
        #     else:
        #         res = max(res, seq)
        #         longest.clear()
        #         seq = 0
        # return res

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # remove the all the characters, up to the duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        # Time complexity : O(n)
        # Space complexity: O(n)