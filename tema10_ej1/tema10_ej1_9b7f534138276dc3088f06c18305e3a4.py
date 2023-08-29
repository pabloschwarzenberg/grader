def mcm(a,b,ab):
    a=int(a)
    b=int(b)
    numeros=[a,b]
    numeros.sort()
    a=numeros[1]
    b=numeros[0]
    def resta(a,b):
        a=a-b
        if a<=b:
            return a
        else:
            return(resta(a,b))
    def mcd(a,b):
        if a-b==0:
            return b
        else:
            d=b
            b=resta(a,b)
            a=d
            return(mcd(a,b))
    mcd=mcd(a,b)
    mcm=(a*b)/mcd
    return mcm

if __name__=="__main__":
    pass
           