# completa el código de la función
from os import system
system ("cls")

def amigos(a, b):
    suma_divisores_a = sum([x for x in range(1, a) if a % x == 0])
    suma_divisores_b = sum([x for x in range(1, b) if b % x == 0])
    if (suma_divisores_a == b) and (suma_divisores_b == a):
        return True
    else:
        return False
           