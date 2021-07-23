class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n=len(nums)
        si=0
        ei=0
        result=0
        count=0
        while ei<n:
            if nums[ei]>=left and nums[ei]<=right:
                count=ei-si+1
                result+=count
            elif nums[ei]<left:
                result+=count
            else:
                si=ei+1
                count=0
            ei+=1
        return result