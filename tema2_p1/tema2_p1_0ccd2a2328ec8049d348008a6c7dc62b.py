import math
 
def es_primo(numero):
    if numero<=1:
        return false
 
    for i in range(2, mat.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return false
    return true