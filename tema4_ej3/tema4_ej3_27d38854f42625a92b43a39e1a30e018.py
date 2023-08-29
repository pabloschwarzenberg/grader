def jerigonzo(string):
    vcls="aeoiuAEOIU"
    r=""
    for i in range(len(string)):
        if string[i] in vcls:
            r+=string[i]+"p"+string[i]
        else:
            r+=string[i]
    return r

      