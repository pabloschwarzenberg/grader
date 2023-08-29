def mcd(c,d):
    if d==0:
       return c       
    else:
        e=c%d
        return mcd(d,e)
def mcm(a,b,ab):
    return (a*b)/mcd(a,b)
        

if __name__=="__main__":
    pass
           