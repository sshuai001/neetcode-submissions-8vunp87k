class MinStack:
    #双栈法
    def __init__(self):
        self.stack = []
        self.min_stack = [2000000000000000000]

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_elem = min(val, self.min_stack[-1])
        self.min_stack.append(min_elem)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
