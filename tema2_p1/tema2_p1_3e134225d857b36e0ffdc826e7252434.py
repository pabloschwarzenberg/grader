# por favor escribe aquí tu función
#def es_primo(numero):
#  return
from pickle import TRUE
def es_primo(numero):
    if numero==1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True