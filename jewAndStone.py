# my gawd solved this problem all by meself


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashMap = {}

        for i in jewels:
            if i not in hashMap:
                hashMap[i] = 0
            for j in stones:
                if j in hashMap:
                    hashMap[j] += 1
        return sum(hashMap.values())
