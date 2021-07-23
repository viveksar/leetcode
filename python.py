class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.count(part)>0:
            ind=s.index(part)
            i1=ind
            i2=i1+len(part)
            left=s[:i1]
            right=''
            if i2>len(s):
                right=''
            else:
                right=s[i2:]
            s=left+right
        return s