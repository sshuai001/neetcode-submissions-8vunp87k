class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        #对于每一个字符串计算字符串的长度+'#'+字符串
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #指示当前处理到哪个字符

        while i < len(s):
            j = i
            # 1. 寻找数字后面的那个 '#'
            while s[j] != '#':
                j += 1
            # 2. 这里的 s[i:j] 就是那个“长度数字”
            # 比如 "12#..."，i 在 '1'，j 在 '#'，s[i:j] 就是 "12"
            length = int(s[i:j])
            #知道字符串的长度之后 j+1是第一个字符的位置,j+1+length是最后一个字符的位置
            content = s[j + 1 : j + 1 + length]

            res.append(content)

            i = j + 1 + length #处理完一个字符串之后下一个字符串开始的位置
        return res

        