def Index(s1, s2, pos=0):
    """ BF算法 """
    i = pos
    j = 0
    while(i < len(s1) and j < len(s2)):
        if(s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if(j >= len(s2)):
        return i - len(s2)
    else:
        return 0


if __name__ == "__main__":
    s1 = "ababcabcacbab"
    s2 = "abcac"
    print(Index(s1, s2))
