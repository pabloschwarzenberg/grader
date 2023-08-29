def mcm(a,b,ab):
    return ab//mcd(a,b)
def mcd(a,b):
    r=a%b
    if r!=0:
        return mcd(b,r)
    return b