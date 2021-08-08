class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result=''
        a=[1]*n
        k=k-n
        i=n-1
        while k>0:
            if k>=25:
                a[i]=26
                k=k-25
                i-=1
            else:
                a[i]+=k
                k=0
        for x in a:
            res=chr(ord('a')-1+x)
            result+=res
        return result