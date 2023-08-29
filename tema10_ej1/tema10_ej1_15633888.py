def mcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return mcd(b,r)

def mcm(a,b,ab):
    return (ab)/mcd(a,b)

if __name__=="__main__":
    pass


           