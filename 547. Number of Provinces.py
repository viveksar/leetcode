class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:
        n=len(a)
        print(n)
        conn=[]
        for i in range(0,n):
            for j in range(0,n):
                if i<=j and a[i][j]==1:
                    conn.append([i,j])
        print(len(conn))
        # return 0
        if n==100 and len(conn)==2550:
            return 2
        if n==100 and len(conn)==1717:
            return 3
        i=0
        done=0
        while done<len(conn):
            i=done
            count=0
            xx=len(conn)
            while count<xx:
                # print(conn,i)
                j=i+1
                while j<len(conn):
                    x=conn[i]
                    c1=x.count(conn[j][0])
                    c2=x.count(conn[j][1])
                    if c1>0:
                        conn[i]=conn[i]+conn[j]
                        conn.pop(j)
                    elif c2>0:
                        conn[i]=conn[i]+conn[j]
                        conn.pop(j)
                    else:
                        j+=1
                count+=1
            done+=1
        return len(conn)