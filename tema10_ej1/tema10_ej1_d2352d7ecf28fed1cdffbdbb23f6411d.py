def mcd(m,n):
    if m>n:
        resto=m%n
        if resto==0:
            return n
        else:
            niu=mcd(n,resto)
            return niu
    else:
        resto = n % m
        if resto == 0:
            return m
        else:
            niu = mcd(m, resto)
            return niu

def mcm(a,b,ab):
    mcm=(ab)/mcd(a,b)
    return mcm

if __name__=="__main__":
    pass
           