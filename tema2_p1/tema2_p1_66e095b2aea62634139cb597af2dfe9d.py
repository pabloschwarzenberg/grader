# por favor escribe aquí tu función
import math
 
def es_primo(numero):

    if (numero<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
 
while True:
    try:
        numero = int(input("inserta un numero o ingresa (0) para salir "))
        if numero==0:
            break
        if es_primo(numero):
            print ("true" % numero)
        else:
            print ("false" % numero)
    except:
        print ("El numero tiene que ser entero")
        break