# por favor escribe aquí tu función
def es_primo(numero):
    for i in range(1,numero):
        if (i!=1 and numero!=i and (numero%i==0)) or (numero==1):
            return False
    if numero==1:
        return False
    return True