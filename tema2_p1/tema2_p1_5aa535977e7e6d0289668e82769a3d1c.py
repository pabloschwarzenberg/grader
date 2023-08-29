import math

def es_primo(numero):
    if(numero<=1):
        return False
    for i in range(2,math.ceil(math.sqrt(numero))+1):
        if (numero%i==0 and i!=numero):
            return False
    return True



numero = 4

if es_primo(numero):
    print(True)

else:
    print(False)
           