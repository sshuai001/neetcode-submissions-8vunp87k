class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        #遍历字符串s中的字符,将他们加入到哈希表
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in t:
            if char not in hashmap:
                return False
            if char in hashmap:
                hashmap[char] -= 1
            if hashmap[char] == 0:
                del(hashmap[char])
        return not hashmap