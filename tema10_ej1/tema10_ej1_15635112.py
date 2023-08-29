def mcm(a,b,ab):
    d=mcd(a,b)
    c=(ab/d)
    return c

def mcd(a,b):
    r=a%b
    if r==0:
        return b
    else:
        return mcd(b,r)

if __name__=="__main__":
    print(mcm(88,44,88*44))
    pass
           