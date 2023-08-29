def MCD(a,b):
    resto = a % b
    if resto == 0:
        return b
    else:
        return MCD(b, resto)


def mcm(a,b,c):
    m = (c)/MCD(a, b)
    return int(m)