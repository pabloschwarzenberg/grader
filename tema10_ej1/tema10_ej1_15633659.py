def mcm(a,b,ab):
    if a>b:
      c=a
      d=b
    elif a<b:
      c=b
      d=a
    def mcd(c,d):
        if c%d==0:
            return (d)
        else:
            return mcd(c,c%d)
    mcm=ab/mcd(c,d)
    return mcm

if __name__=="__main__":
    pass
           