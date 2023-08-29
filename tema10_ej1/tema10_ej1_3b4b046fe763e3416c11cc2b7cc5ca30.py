def mcm(a,b,ab):
    return (ab)/mcd(a,b)
def mcd (a,b):
    q=a//b
    r=a%b
    if r==0:
        return b
    else:
        return mcd(b,r)

if __name__=="__main__":
    pass
           