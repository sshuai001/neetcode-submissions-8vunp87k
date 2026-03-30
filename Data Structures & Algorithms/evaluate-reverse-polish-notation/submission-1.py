class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ('+', '-', '*', '/')

        for item in tokens:
            if item in ops:
                #先弹出的是右操作数,后弹出的是左操作数
                right =  stack.pop()
                left = stack.pop()

                if item == '+':
                    stack.append(left + right)
                elif item == '-':
                    stack.append(left - right)
                elif item == '*':
                    stack.append(left * right)
                elif item == '/':
                    stack.append(int(left / right)) #使用int取整
            else:
                stack.append(int(item))
        return stack[-1]