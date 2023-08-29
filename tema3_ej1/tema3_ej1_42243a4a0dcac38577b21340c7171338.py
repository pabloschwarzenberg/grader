a=int(input("ingrese un numero: "))
def suma_divisores(a):
    suma = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            suma += divisor
    return suma
if suma_divisores(a) != 1:
    print(suma_divisores(a))
else:
    print("el numero es primo")

           