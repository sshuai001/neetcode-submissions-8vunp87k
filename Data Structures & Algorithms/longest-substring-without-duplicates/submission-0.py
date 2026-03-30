class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        length = 1
        L = 0
        for R in range(1, len(s)):
            if s[R] in s[L:R]:
                #L移动到窗口中重复字符的下一个位置, 
                #s[L:R].index(s[R])是窗口中重复字符相对L的偏移
                L = L + s[L:R].index(s[R]) + 1
            length = max(length, (R - L + 1))
        return length
