class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        #栈中有多少个开括号都无所谓
        for char in s:
            #如果是闭括号,将栈顶元素弹出比对
            if char in mapping and stack:
                top_elem = stack.pop()
                if top_elem != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack