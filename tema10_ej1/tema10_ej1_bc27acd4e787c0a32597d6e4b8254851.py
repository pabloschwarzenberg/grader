def mcm(a,b,ab):
    def MCD(a,b):
        if b==0:
           return a
        else:           
           if a>b:
            c=a
            d=b
           else:
             c=b
             d=a
           r=c%d
           return MCD(d,r)
    m=ab/MCD(a,b)
    return m


if __name__=="__main__":
    pass
           