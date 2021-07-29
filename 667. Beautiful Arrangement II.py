class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        a=[]
        b=[]
        for i in range(1,n+1):
            # a.append(i)
            if i<=k+1:
                b.append(i)
            else:
                a.append(i)
        result=[]
        front=1
        while len(b)>0:
            if front==1:
                result+=[b[0]]
                b.pop(0)
                front=0
            else:
                result+=[b[-1]]
                b.pop(-1)
                front=1
            # print(result,a,b)
        result+=a
        return result