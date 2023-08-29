# por favor escribe aquí tu función
def es_primo(numero):
    if numero<2:
        return False
    for i in range (2,numero,1):
        resto=numero%i
        if resto==0:
           return False
    else:
        return True
           