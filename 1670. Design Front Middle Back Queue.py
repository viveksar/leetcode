class FrontMiddleBackQueue:
    a = []

    def __init__(self):
        self.a = []

    def pushFront(self, val: int) -> None:
        self.a = [val] + self.a
        # print('pushfront ',end=" ")
        # print(self.a)

    def pushMiddle(self, val: int) -> None:
        n = len(self.a)
        self.a.insert(n // 2, val)
        # print('pushmiddle',end=" ")
        # print(self.a)

    def pushBack(self, val: int) -> None:
        self.a = self.a + [val]
        # print('pushback ',end=" ")
        # print(self.a)

    def popFront(self) -> int:
        # print(self.a)
        if len(self.a) == 0:
            return -1
        x = self.a.pop(0)
        # print('pop fornt ',end=" ")
        # print(self.a)
        return x

    def popMiddle(self) -> int:
        n = len(self.a)
        print(self.a)
        if n % 2 == 0:
            mid = n // 2
            mid = mid - 1
        else:
            mid = n // 2
        if len(self.a) == 0:
            return -1
        x = self.a.pop(mid)
        # print('popmiddle ',end=" ")
        # print(self.a)
        return x

    def popBack(self) -> int:
        print(self.a)
        if len(self.a) == 0:
            return -1
        x = self.a.pop(-1)
        # print('pop back',end=" ")
        # print(self.a)
        return x

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()