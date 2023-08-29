def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)
def mcm(a,b,ab):
    return (a*b)/mcd(a,b)     