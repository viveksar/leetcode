class Solution:
    def magicalString(self, n: int) -> int:
        curr='122'
        ind=2
        while len(curr)<n:
            if curr[ind]=='1':
                if curr[-1]=='1':
                    curr+='2'
                else:
                    curr+='1'
            else:
                if curr[-1]=='1':
                    curr+='22'
                else:
                    curr+='11'
            ind+=1
        req=curr[:n]
        # print(req)
        return req.count('1')