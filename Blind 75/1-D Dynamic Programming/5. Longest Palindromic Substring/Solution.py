class Solution:
    def longestPalindrome(self, s: str) -> str:

        # start a pointer on both sides
        # if far right isnt equal to far left decrement the right, until it is equal
        # nope this approach wont work because it will only find the largest substring from the beggining

        res = ""
        resLen = 0 

        for i in range(len(s)):
            # even length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # odd length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
        # time complexity: O(n)
        # space complexity: O(1)