def mcd(a,b):
    if b==0:
        return a
    else:
        b1=b
        b=a%b
        a=b1
        return mcd(a,b)
    
def mcm(a,b,ab):
    m=mcd(a,b)
    mc=ab/m
    return mc

if __name__=="__main__":
    print(mcm(88,44,88*44))