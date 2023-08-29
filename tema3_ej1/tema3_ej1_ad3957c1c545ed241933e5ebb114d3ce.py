# completa el código de la función

def suma_divisores(a,b):
    numeros = []
    for i in range (1,a):
        if a % i == 0:
            numeros.append(i)
    for j in range (1,b):
        if b % j == 0:
            numeros.append(j)
   return int(sum(numeros))

def esPrimo():
    if (suma_divisores(a,b) % 2) == 0:
        return False
    elif divisores(a,b) == 1:
        return False
    else:
        return True
