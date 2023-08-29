def mcd(a,b):
    if b == 0:
        return a
    p_entera = a//b
    resto = a - b*p_entera
    return mcd(b,resto)

def mcm(a,b,c):
    h = int(mcd(a,b))
    resultado = c/h
    return resultado


if __name__=="__main__":
    pass
           