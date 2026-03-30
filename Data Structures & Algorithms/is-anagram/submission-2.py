class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}
        for char in s:
            #将字符串s中的每一个char加入到字典中
            hashmap[char] = hashmap.get(char , 0) + 1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
        return not hashmap
                
            