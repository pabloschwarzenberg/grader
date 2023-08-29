def mcm(a,b,ab):
    return a*b/mcd(a,b)

def mcd(a,b):
    if a==b:
        return a
    else:
        if a>b:
            return mcd(a-b,b)
        else:
            return mcd(a, b-a)
