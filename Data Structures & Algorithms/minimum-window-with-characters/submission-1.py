class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
         
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1

                while have == need:
                    if (r - l + 1) <res_len:
                        res = [l, r]
                        res_len = r - l + 1
                    #弹出最左侧的元素
                    window[s[l]] -= 1
                    if s[l] in countT and  window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""



