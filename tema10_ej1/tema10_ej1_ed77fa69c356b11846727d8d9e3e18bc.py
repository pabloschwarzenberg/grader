def mcd(a,b):
    if b == 0:
        return a

    elif a == 0:
        return b

    elif b > a:
        c = b%a
        return mcd(a,c)

    elif b < a:
        c = a%b
        return mcd(b,c)
    
def mcm(a,b,ab):
    c = ab//mcd(a,b)
    return c
    