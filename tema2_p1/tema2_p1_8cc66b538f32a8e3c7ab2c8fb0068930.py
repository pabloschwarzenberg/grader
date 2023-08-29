# por favor escribe aquí tu función
def es_primo(numero):
    if numero!=1 and (numero==2 or numero==3 or numero==5):
        return True
    elif numero!=1 and numero%2!=0 and numero%3!=0 and numero%5!=0:
        return True
    else:
        return False