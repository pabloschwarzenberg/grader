# completa el código de la función
import math

def suma_divisores(a):

    suma = 0
    esPrimo = False

    for i in range(1,a):
        if a%i == 0:
            suma += i

    if suma == 1:
        esPrimo = True
    return (suma,esPrimo)

if __name__ == "__main__":

    a = int(input('a: '))
    print(suma_divisores(a))
