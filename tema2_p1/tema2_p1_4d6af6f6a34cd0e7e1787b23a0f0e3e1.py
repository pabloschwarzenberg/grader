# por favor escribe aquí tu función
def es_primo(numero):
    if numero==0 or numero==1:
        return False
    for i in (2,numero):
        if numero%i==0:
            return False
        return True

           