def mcd(a,b):
    resto = a%b
    if resto == 0:
        return b
    else:
        return mcd(b, resto)

def mcm(a,b,ab):
    mcm = (ab)/mcd(a,b)
    return mcm

if __name__=="__main__":
    pass
           