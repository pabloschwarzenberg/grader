def mcm(a,b,ab):
    d=mcd(a,b)
    c=(ab/d)
    return c
    
def mcd(a,b):
    r=a%b
    a=b
    b=r
    if b==0:
        return a
        mcd(a,b)
if __name__=="__main__":
    print(mcm(88,44,88*44))
    pass