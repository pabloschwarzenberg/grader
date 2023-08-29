# por favor escribe aquí tu función
import math
 
def es_primo(n):
    if (n<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if(n%i==0 and i!=n):
            return False
    return True
 
while True:
    try:
        n = int(input("ingresa un numero o ingresa (0) para salir "))
        if n==0:
            break
        if es_primo(n):
            print("el numero %s es primo" % n)
        else:
            print("el numero %s no es primo" % n)
    except:
        print("el numero tiene que ser un entero")
        break