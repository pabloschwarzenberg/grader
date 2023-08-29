def mcd(a,b):
    if a>b:
        r=a%b
        if r==0:
            return b
        return mcd(b,r)
    elif a<b:
        r=b%a
        if r==0:
            return a
        return mcd(a,r)
    
def mcm(a,b,ab):
    return (a*b)/mcd(a,b)
    

if __name__=="__main__":
    pass
           