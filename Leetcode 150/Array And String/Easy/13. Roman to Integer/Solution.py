class Solution:
    def romanToInt(self, s: str) -> int:

        val = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # my solution (it works)

        # res = val[s[-1]]
        # for i in range(len(s) - 2, -1, -1):
        #     check = s[i + 1]
        #     if s[i] == 'I' and (check == 'X' or check == 'V'):
        #         res -= 1
        #     elif s[i] == 'X' and (check == 'L' or check == 'C'):
        #         res -= 10
        #     elif s[i] == 'C' and (check == 'D' or check == 'M'):
        #         res -= 100
        #     else:
        #         res += val[s[i]]
        # return res

        # neetcode solution

        res = 0

        for i in range(len(s)):
             if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:
                res -= val[s[i]]
             else:
                res += val[s[i]]
        return res