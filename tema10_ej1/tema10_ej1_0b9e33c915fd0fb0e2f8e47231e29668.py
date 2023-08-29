def mcd(d,n):
    if d > n:
        if d % n == 0:
            return n
        else:
            c = d % n
            return mcd(n,c)
    if n > d:
        if n % d == 0:
            return d
        else:
            c = n % d
            return mcd(d,c)

def mcm(a,b,ab):
    ab = a*b
    c = (ab)/(mcd(a,b))
    return c
if __name__=="__main__":
    pass
           