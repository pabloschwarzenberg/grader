def jerigonzo(p):
    vocal="aeoiuAEOIU"
    r=""
    for x in range(len(p)):
        if p[x] in vocal:
            r+=p[x]+"p"+p[x]
        else:
            r+=p[x]
    return r
