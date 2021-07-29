class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n==1:
            return [1]
        result=[1,2]
        if n==2:
            return result
        count=2
        while count<n:
            odd=[]
            even=[]
            for i in range(0,len(result)):
                o=2*result[i]-1
                if o<=n:
                    odd.append(o)
                e=2*result[i]
                if e<=n:
                    even.append(e)
            result=odd+even
            count+=1
        return result