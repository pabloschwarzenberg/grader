def mcd(a,b):
    if b == 0:
        return a 
    else:
        return mcd(b,a%b)

def mcm (a,b,c):
    c = a*b
    mincm = c /(mcd(a,b))
    return mincm
