class Solution:
    def invert(self, a):
        final = ''
        for x in a:
            if x == '1':
                final += '0'
            else:
                final += '1'
        return final

    def reverse(self, a):
        return a[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        a = [-1] * (n + 1)
        a[1] = '0'
        for i in range(2, n + 1):
            x = a[i - 1] + '1' + self.reverse(self.invert(a[i - 1]))
            a[i] = x
        final = a[n]
        return final[k - 1]