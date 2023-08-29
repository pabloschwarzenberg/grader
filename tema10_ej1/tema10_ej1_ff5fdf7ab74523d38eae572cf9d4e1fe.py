def mcd(a,b):
    if a>=b:
        r=a%b
        if r==0:
            return b
        else:
            return mcd(b,r)
    else:
        r=b%a
        if r==0:
            return(a)
        else:
            return mcd(a,r)

def mcm(a,b,ab):
    return a*b/mcd(a,b)