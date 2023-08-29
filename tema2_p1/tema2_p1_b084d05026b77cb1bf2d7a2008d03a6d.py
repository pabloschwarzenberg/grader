# por favor escribe aquí tu función
def es_primo(numero):
    prim= False
    numero= int(numero)
    if numero==1:
        prim= False
    elif numero ==2:
        prim= True
    else:
        for i in range(2, numero):
            if numero%i==0 and numero!=2:
                prim= False
                break
            elif numero%i!=0:
                prim= True
    return (prim)
