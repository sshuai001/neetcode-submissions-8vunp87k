class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        #初始化s1
        cnt1 = [0] * 26
        for char in s1:
            cnt1[ord(char) - ord('a')] += 1
        #初始化窗口
        window = [0] * 26
        for i in range(n1):
            window[ord(s2[i]) - ord('a')] += 1
        #开始滑动
        for i in range(n2 - n1):
            if window == cnt1:
                return True
            else:
                window[ord(s2[i]) - ord('a')] -= 1
                window[ord(s2[i + n1]) - ord('a')] += 1

        return window == cnt1


