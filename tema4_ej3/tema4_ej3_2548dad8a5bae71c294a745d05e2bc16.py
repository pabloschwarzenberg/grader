def jerigonzo(string):
    vcls="aeoiuAEOIU"
    r=""
    for x in range(len(string)):
        if string[x] in vcls:
            r+=string[x]+"p"+string[x]
        else:
            r+=string[x]
    return r   