class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, count_s = {}, {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        have, need = 0, len(count_t)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            count_s[char] = count_s.get(char, 0) + 1

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
                    

