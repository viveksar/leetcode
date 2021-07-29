class Solution:
    res = []

    def per(self, a, arr):
        if len(a) == 0:
            self.res.append(arr)
        else:
            j = len(arr) + 1
            for i in range(0, len(a)):
                if i == 0:
                    if a[i] % j == 0 or j % a[i] == 0:
                        self.per(a[1:], arr + [a[i]])
                elif i == len(a) - 1:
                    if a[i] % j == 0 or j % a[i] == 0:
                        self.per(a[:-1], arr + [a[i]])
                else:
                    if a[i] % j == 0 or j % a[i] == 0:
                        self.per(a[:i] + a[i + 1:], arr + [a[i]])

    def countArrangement(self, n: int) -> int:
        a = []
        self.res = []
        for x in range(1, n + 1):
            a.append(x)
        self.per(a, [])
        # print(self.res)
        # print(len(self.res
        return len(self.res)class Solution:
    res=[]
    def per(self,a,arr):
        if len(a)==0:
            self.res.append(arr)
        else:
            j=len(arr)+1
            for i in range(0,len(a)):
                if i==0 :
                    if a[i]%j==0 or j%a[i]==0:
                        self.per(a[1:],arr+[a[i]])
                elif i==len(a)-1:
                    if a[i]%j==0 or j%a[i]==0:
                        self.per(a[:-1],arr+[a[i]])
                else:
                    if a[i]%j==0 or j%a[i]==0:
                        self.per(a[:i]+a[i+1:],arr+[a[i]])

    def countArrangement(self, n: int) -> int:
        a=[]
        self.res=[]
        for x in range(1,n+1):
            a.append(x)
        self.per(a,[])
        # print(self.res)
        # print(len(self.res
        return len(self.res)