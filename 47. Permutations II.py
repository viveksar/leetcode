class Solution:
    result = []

    def manage(self, a, arr):
        if len(a) == 0 and (arr not in self.result):
            self.result.append(arr)
        for i in range(0, len(a)):
            x = arr + [a[i]]
            if i == 0:
                y = a[1:]
                self.manage(y, x)
            elif i == len(a) - 1:
                y = a[:-1]
                self.manage(y, x)
            else:
                y = a[:i] + a[i + 1:]
                self.manage(y, x)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.manage(nums, [])
        print(self.result)
        return self.result