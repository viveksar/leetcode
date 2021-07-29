class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start=[]
        end=[]
        person=[]
        for x in trips:
            person.append(x[0])
            start.append(x[1])
            end.append(x[2])
        a={}
        for i in range(0,len(start)):
            if start[i] not in a:
                a[start[i]]=person[i]
            else:
                a[start[i]]+=person[i]
        for i in range(0,len(start)):
            if end[i] not in a:
                a[end[i]]=-person[i]
            else:
                a[end[i]]-=person[i]
        # time=[]
        # for x in a:
        #     time.append(x)
        # time.sort()
        time=start+end
        time=list(dict.fromkeys(time))
        time.sort()
        # print(time)
        # print(a)
        for i in range(1,len(time)):
            a[time[i]]+=a[time[i-1]]
        for x in time:
            if a[x]>capacity:
                return False
        return True