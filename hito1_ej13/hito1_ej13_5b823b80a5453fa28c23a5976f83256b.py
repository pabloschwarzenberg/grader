#Factores Primos
def esPrimo(n):
    if n > 1:
        if n != 2 or n != 3:
            for i in range(n-3):
                if n % (i+2) == 0:
                    return False
        return True
    return False

def esFactor(n, x):
    if n % x == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

for i in range(numero):
    n = i+1
    if esPrimo(n) and esFactor(numero, n):
        print(n)