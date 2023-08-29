# por favor escribe aquí tu función
import math
def es_primo(numero):
    if (numero<2):
        return False
 
    for i in range(2,numero):
        if(numero%i==0 and i!=numero):
            return False
    return True
