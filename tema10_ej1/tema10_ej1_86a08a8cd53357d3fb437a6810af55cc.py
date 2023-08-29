def mcm(a,b,ab):
    if a>=b:
        mayor = a
        menor = b
    else:
        mayor = b
        menor = a

    def mcd(a,b):
        resto = a%b
        if resto == 0:
            return b
        else:
            return mcd(b,resto)

    return int(ab/mcd(a,b))

if __name__=="__main__":
    pass
           