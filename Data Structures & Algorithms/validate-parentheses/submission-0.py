class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #构建括号之间的映射
        mapping = {')':'(',']':'[','}':'{'}

        for char in s:
            if char in mapping:
                #如果是右括号,先检查栈是否为空,再弹出栈顶元素看是否匹配
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                #如果是左括号,直接加入栈
                stack.append(char)
        return not stack