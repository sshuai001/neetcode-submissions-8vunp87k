class Solution:
    def isPalindrome(self, s: str) -> bool:
        #初始化左右两个指针
        left = 0
        right = len(s) - 1

        while left < right:
            # 1. 跳过左侧非字母数字字符
            while left < right and not s[left].isalnum():
                left += 1
            # 2. 跳过右侧非字母数字字符
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True