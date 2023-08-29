def jerigonzo(s):
    vcls="aeoiuAEOIU"
    r=""
    for x in range(len(s)):
        if s[x] in vcls:
            r+=s[x]+"p"+s[x]
        else:
            r+=s[x]
    return r

      