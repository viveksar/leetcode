class Solution:
    def optimalDivision(self, a: List[int]) -> str:
        result=''
        n=len(a)
        if n==1:
            return str(a[0])
        if n==2:
            return  str(a[0])+'/'+str(a[1])
        result=str(a[0])+'/('+str(a[1])
        for i in range(2,n):
            result+='/'+str(a[i])
        result+=')'
        return result