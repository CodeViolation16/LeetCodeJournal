# MY GOD I HATE THIS EDGE CASES

class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        summ = 0
        length = len(s)
        i = 0

        while i < length:
            if i < length - 1 and hashMap[s[i]] < hashMap[s[i+1]]:
                summ += hashMap[s[i + 1]] - hashMap[s[i]]
                i+= 2
            else:
                summ += hashMap[s[i]]
                i+= 1
        return summ 
