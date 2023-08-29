def mcm(a,b,ab):
    r=a*b/mcd(a,b)
    return r
    
def mcd(a,b):
    d=1
    listo=False
    while listo==False:
        if a%d==0 and b%d==0:
            listo=True
            return d
        else:
            d=d+1
    

if __name__=="__main__":
    pass
           