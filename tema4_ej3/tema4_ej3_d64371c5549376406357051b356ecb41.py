def jerigonzo(b):
    vcls="aeoiuAEOIU"
    a=""
    for x in range(len(b)):
        if b[x] in vcls:
            a+=b[x]+"p"+b[x]
        else:
            a+=b[x]
    return a

      