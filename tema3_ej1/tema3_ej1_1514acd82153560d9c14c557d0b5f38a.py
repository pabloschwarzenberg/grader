#Suma de los divisores de un número
def suma_divisores(a):
    suma = 0
    primo=()

    for i in range(1, a):
        if a % i == 0:
            suma += i

    return suma, suma==1
