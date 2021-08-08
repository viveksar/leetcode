class Solution:
    def waysToMakeFair(self, a: List[int]) -> int:
        os=0
        es=0
        for i in range(0,len(a)):
            if i%2==0:
                es+=a[i]
            else:
                os+=a[i]
        pe=0
        po=0
        i=0
        count=0
        while i<len(a):
            if i%2==0:
                es=es-a[i]
                ce=pe+os
                co=po+es
                if ce==co:
                    count+=1
                pe+=a[i]
            else:
                os=os-a[i]
                ce=pe+os
                co=po+es
                if ce==co:
                    count+=1
                po+=a[i]
            i+=1
        return count