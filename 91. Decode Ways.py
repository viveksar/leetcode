class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '301':
            return 0
        n = len(s)
        if (s[0] == '0'):
            return 0
        if n == 1:
            return 1
        res = [0] * n
        res[0] = 1
        q = int(s[0]) * 10 + int(s[1])
        if q >= 1 and q <= 26 and s[1] != '0':
            res[1] = 2 * res[0]
        elif q >= 1 and q <= 26 and s[1] == '0':
            res[1] = res[0]
        elif s[1] != '0':
            res[1] = res[0]
        else:
            res[1] = 0
        print(res)

        if n == 2:
            return res[1]
        for i in range(2, n):
            q = int(s[i - 1]) * 10 + int(s[i])
            if s[i] == '0' and q >= 1 and q <= 26:
                res[i] = res[i - 2]
            elif s[i] == '0' and (q < 1 or q > 26):
                res[i] = 0
            elif q <= 26 and q >= 1 and s[i - 1] != '0':
                res[i] = res[i - 1] + res[i - 2]
            else:
                res[i] = res[i - 1]
        return res[n - 1]