def mcd(a,b):
    if a>b:
        c=a%b
        c1=a/b
        if c!=0:
            return mcd(b,c)
        else:
            return b
    else:
        c=b%a
        c1=b/a
        if c!=0:
            return mcd(a,c)
        else:
            return a

def mcm(a,b,ab):
    resultado=(a*b)/mcd(a,b)
    return resultado
    pass

if __name__=="__main__":
    pass
           