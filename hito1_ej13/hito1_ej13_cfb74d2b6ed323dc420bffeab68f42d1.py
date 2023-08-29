from math import sqrt

def factores_primos(num):

    factores_primos_lista = []
    while num % 2 == 0:
        factores_primos_lista.append(2)
        num /= 2
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            factores_primos_lista.append(i)
            num /= i
    if num > 2:
        factores_primos_lista.append(int(num))
    factores_primos_lista=(sorted(factores_primos_lista))
    for x in factores_primos_lista:
        print(x)

val = int(input('Ingrese el número:'))
factores_primos(val)
