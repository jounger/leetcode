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
        self.min = self.stack[-1][1] if len(self.stack) > 0 else None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack2:
    def __init__(self):
        self.list = LinkedList()

    def push(self, val: int) -> None:
        self.list.push(val)

    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        if self.list.head == None:
            raise ValueError("No value")
        return self.list.head.val

    def getMin(self) -> int:
        if self.list.head == None:
            raise ValueError("No value")
        return self.list.head.min


class LinkedNode:
    def __init__(self, val: int, min_val: int):
        self.val = val
        self.min = min_val
        self.next: LinkedNode | None = None
        self.prev: LinkedNode | None = None


class LinkedList:
    def __init__(self):
        self.head: LinkedNode | None = None

    def pop(self):
        if self.head == None:
            return
        self.head = self.head.prev

    def push(self, val):
        if self.head == None:
            self.head = LinkedNode(val, val)
            return

        node = LinkedNode(val, min(self.head.min, val))
        node.prev = self.head
        self.head.next = node
        self.head = self.head.next


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
