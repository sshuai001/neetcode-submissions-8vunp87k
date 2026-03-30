class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ('+','-','*','/')

        for char in tokens:
            if char in ops:
                right = stack.pop()
                left = stack.pop()
                if char == '+':
                    stack.append(left + right)
                if char == '-':
                    stack.append(left - right)
                if char == '*':
                    stack.append(left * right)
                if char == '/':
                    stack.append(int(left / right))
            else:
                stack.append(int(char))
        return stack[-1]

