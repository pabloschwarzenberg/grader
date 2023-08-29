# por favor escribe aquí tu función
import math
def es_primo(x):
    if (x<=1):
        return False
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if(x % i==0 and i!=x):
            return False
    return True
while True:
    try:
        x = int(input("escriba un numero: ", ))
        if x==0:
            break
        if primo(x):
            print("el numero %s es primo" % x)
            break
        else:
            print("el numero %s no es primo" % x)
            break
    except:
        print("el numero tiene que ser entero")
        break