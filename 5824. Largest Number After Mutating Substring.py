class Solution:
    def maximumNumber(self, s: str, change: List[int]) -> str:
        start = 0
        a = list(s)
        for i in range(0, len(a)):
            a[i] = int(a[i])

        find = 0
        for i in range(0, len(a)):
            if find == 0 and a[i] < change[a[i]]:
                find = 1
                a[i] = change[a[i]]
            elif find == 1 and a[i] < change[a[i]]:
                a[i] = change[a[i]]
            elif find == 1 and a[i] > change[a[i]]:
                find = 0
                break
        res = ''
        for x in a:
            res += str(x)
        return res