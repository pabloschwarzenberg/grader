def mcm(a,b,ab):
  mcm=(a*b)/mcd(a,b,1,1)
  return mcm

def mcd(a,b,c,d):
    if c>a or c>b:
        return d
    else:
        if ((a/c)-(a//c))==0 and ((b/c)-(b//c))==0:
            d=c
        return mcd(a,b,c+1,d)
