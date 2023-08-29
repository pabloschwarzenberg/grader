def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b,a-b*(a//b))

def mcm(a,b,nada):
    a=int(a)
    b=int(b)
    if a > b:
        return a*b/mcd(a,b)
    else:
        return a*b(mcd(b,a))
if __name__=="__main__":
    pass
           