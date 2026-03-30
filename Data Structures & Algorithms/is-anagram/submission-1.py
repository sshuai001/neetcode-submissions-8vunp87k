class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        #遍历字符串s中的字符,将他们加入到哈希表
        for char in s:
            #如果哈希表中存在键则值+1,如果不存在置为0再+1
            hashmap[char] = hashmap.get(char , 0) + 1 
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
        return not hashmap