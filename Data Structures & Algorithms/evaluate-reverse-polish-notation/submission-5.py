class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ('+','-','*','/')

        for char in tokens:
            if char in ops:
                # 1. 只有遇到运算符，才需要“消耗”栈里的数字
                # 注意：先弹出的是右操作数，后弹出的是左操作数（减法和除法对顺序敏感）
                right = stack.pop()
                left = stack.pop()

                if char == '+':
                    stack.append(left + right)
                if char == '-':
                    stack.append(left - right)
                if char == '*':
                    stack.append(left * right)
                if char == '/':
                    stack.append(int(left / right)) #取整
            else:
                stack.append(int(char)) #str -> int 
        return stack[-1]

