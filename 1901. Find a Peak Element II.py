#leetcode problem-1901
class Solution:
    def isPeak(self, a, i, j):
        if a[i][j] > a[i - 1][j] and a[i][j] > a[i + 1][j] and a[i][j] > a[i][j + 1] and a[i][j] > a[i][j - 1]:
            return True

    def findPeakGrid(self, a: List[List[int]]) -> List[int]:
        for i in range(0, len(a)):
            a[i] = [-1] + a[i] + [-1]
        x = [-1] * len(a[0])
        a = [x] + a + [x]
        n = len(a)
        m = len(a[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if self.isPeak(a, i, j):
                    return [i - 1, j - 1]class Solution:
    def isPeak(self,a,i,j):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]:
            return True

    def findPeakGrid(self, a: List[List[int]]) -> List[int]:
        for i in range(0,len(a)):
            a[i]=[-1]+a[i]+[-1]
        x=[-1]*len(a[0])
        a=[x]+a+[x]
        n=len(a)
        m=len(a[0])
        for i in range(1,n-1):
            for j in range(1,m-1):
                if self.isPeak(a,i,j):
                    return [i-1,j-1]