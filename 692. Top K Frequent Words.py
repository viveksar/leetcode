class Solution:
    def topKFrequent(self, word: List[str], k: int) -> List[str]:
        a={}
        freq=[]
        for x in word:
            if x not in a:
                a[x]=1
            else:
                a[x]+=1
        b={}
        for x in a:
            if a[x] not in b:
                b[a[x]]=[x]
            else:
                b[a[x]].append(x)
        freq=[]
        for x in b:
            freq.append(x)
        freq.sort()
        freq=freq[::-1]
        i=0
        result=[]
        while len(result)<k:
            fre=freq[i]
            arr=b[fre]
            arr.sort()
            for x in arr:
                if len(result)<k:
                    result.append(x)
                else:
                    break
            i+=1
        return result