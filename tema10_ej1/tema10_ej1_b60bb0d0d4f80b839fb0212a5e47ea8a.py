def mcd(a,b):
    #con a mayor que b
    c=a
    while c>=0:
        c=a-b
        a=c
        if c==0:
            return b
        if c<0:
            c=c+b
            return mcd(b,c)
def mcm(a,b,ab):
    mcm=ab/mcd(a,b)
    return int(mcm)
    

if __name__=="__main__":
    pass
           