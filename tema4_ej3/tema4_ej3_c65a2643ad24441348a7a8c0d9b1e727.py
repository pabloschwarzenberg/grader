
def jerigonzo(s):
    K="aeoiuAEOIU"
    L=""
    for x in range(len(s)):
        if s[x] in K:
            L+=s[x]+"p"+s[x]
        else:
            L+=s[x]
    return L

      