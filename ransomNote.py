class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        for i in magazine:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        for i in ransomNote:
            if i not in hashMap:
                return False
            elif hashMap[i] == 1:
                del hashMap[i]
            else:
                hashMap[i] -= 1
        return True
