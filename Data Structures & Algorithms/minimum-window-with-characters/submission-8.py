class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count_t: 目标频率表，count_s: 窗口当前频率表
        count_t, count_s = {}, {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        # need: 我们需要达标的字符“种类”数
        # have: 当前窗口内已经达到 count_t 要求的字符“种类”数
        have, need = 0, len(count_t)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            count_s[char] = count_s.get(char, 0) + 1
            # 如果这个字符在 t 中存在，且数量刚好达到 t 的要求
            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            while have == need:
                if (r - l + 1) <resLen:
                    res = [l, r]
                    resLen = r - l + 1

                left_char = s[l]
                count_s[left_char] -= 1
                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    have -= 1
                l += 1

        l, r = res 

        return s[l:r + 1] if resLen != float('infinity') else ""
                    

