import math
def es_primo(j):
    if (j <= 1):
        return False
    for i in range(2, math.ceil(math.sqrt(j)) + 1):
        if (j % i == 0 and i != j):
            return False
    return True
while True:
    try:
        j = int(input("inserta un numero o ingresa (0) para salir "))
        if j == 0:
            break
        if es_primo(j):
            print("True")
            break
        else:
            print("False")
            break
    except:
        print("El numero tiene que ser entero")
        break