# por favor escribe aquí tu función
import math
def es_primo(numero):
    if (numero<=1):
        return False
    for x in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%x==0 and x!=numero):
            return False
    return True
