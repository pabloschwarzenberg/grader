# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
        return False
    k=2
    while k<numero:
        if numero%k==0:
            return False
        k=k+1
    return True

           