def mcm(a,b,c):
    mcm = c/mcd(a,b)
    return mcm

def mcd(a, b):
    if b == 0 and a != 0:
        return a
    elif a == 0 and b != 0:
        return b
    else:
        return mcd(b, a % b)
           