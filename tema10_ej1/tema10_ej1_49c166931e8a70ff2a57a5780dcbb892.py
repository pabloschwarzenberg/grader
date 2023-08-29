def mcd(a,b):
    if b==0:
        return a
    r=a%b
    return mcd(b,r)
def mcm(a,b,ab):
    n=ab/(mcd(a,b))
    return n

if __name__=="__main__":
    pass
           