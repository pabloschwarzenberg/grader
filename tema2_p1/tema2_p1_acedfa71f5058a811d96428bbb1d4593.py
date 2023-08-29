# por favor escribe aquí tu función
def es_primo(numero):
    for d in range (2,numero):

        if numero%d==0:
            es_primo=False
            return False
        else:
            es_primo=True
            return True
    if numero==1:
        es_primo=False
        return False