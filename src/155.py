# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min == None or self.min > val:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[len(self.stack) -
                              1][1] if len(self.stack) > 0 else None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
