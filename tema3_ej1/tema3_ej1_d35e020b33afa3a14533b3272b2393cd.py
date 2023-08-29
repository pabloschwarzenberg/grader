# completa el código de la función
def suma_divisores(a):
    miau=0
    numero=1
    if a==1 or a==0:
        return miau,False
    else:
        while numero<a:
            if a%numero==0:
                miau+=numero
            numero+=1
    if miau==1:
        return miau, True
    else:
        return miau, False