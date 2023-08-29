import math
def mcd(a,b):
    c = max(a,b)
    d = min(a,b)
    while d!=0:
        mcd = d
        d = c%d
        c = mcd
    return mcd
    
def mcm(a,b,ab):
    c = max(a,b)
    d = min(a,b)
    mcm = (ab / mcd(c,d))
    return mcm
    
    

if __name__=="__main__":
    pass
           