import math
def es_primo(p):
    if (p<=1):
        return False
    for i in range(2, math.ceil(math.sqrt(p))+1):
        if(p%i==0 and i!=p):
            return False
    return True
while True:
    try:
        p = int(input())
        if p==0:
            break
        if es_primo(p):
            print("el numero %s es primo" % p)
        else:
            print("el numero %s no es primo" % p)
    except:
        print("el numero tiene que ser un entero")
        break