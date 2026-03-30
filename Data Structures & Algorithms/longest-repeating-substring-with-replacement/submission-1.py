class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {} 
        L = 0
        max_length = 0
        max_f = 0
        
        for R in range(len(s)):
            #更新当前字符的计数
            char = s[R]
            counts[char] = counts.get(char, 0) + 1
            max_f = max(max_f, counts[char])
            #说明当前窗口不满足修改k个较少的字符就能全部变为同一字符
            while (R - L + 1) - max_f > k:
                counts[s[L]] -= 1
                L += 1
            max_length = max(max_length,(R - L + 1))
            
        return max_length

 