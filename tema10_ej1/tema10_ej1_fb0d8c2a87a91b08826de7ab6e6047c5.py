def mcd(a,b):
    if a>b:
        lul=a%b
        if a%lul==0 and b%lul==0:
            return lul
        else:
            lal=mcd(b,lul)
            return lal
    elif a==b:
        return a
    else:
        lul = b % a
        if a % lul == 0 and b % lul == 0:
            return lul
        else:
            lal = mcd(a, lul)
            return lal
def mcm(a,b,ab):
    mcd1=mcd(a,b)
    return (ab/mcd1)