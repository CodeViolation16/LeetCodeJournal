 res = []
        len1, len2 = len(word1), len(word2)
        i = 0
        while i < len1 and i < len2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        if len1 > i:
            res.append(word1[i:])
        if  len2 > i:
            res.append(word2[i:])
        return "".join(res)

# The while loop really solve the mysticism here. Append alternatively 
