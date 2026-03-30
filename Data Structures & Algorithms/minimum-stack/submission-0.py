class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [200000000000000000000000]

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(val, self.min_stack[-1])
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
