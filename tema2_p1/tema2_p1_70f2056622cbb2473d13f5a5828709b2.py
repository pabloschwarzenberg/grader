# por favor escribe aquí tu función
from os import system
system ("cls")

def es_primo(numero):
    """Verifica si un número dado es primo o no."""
    # 1 no es primo
    if numero == 1:
        return False
    
    # 2 y 3 son primos
    if numero == 2 or numero == 3:
        return True
    
    # los números pares mayores a 2 no son primos
    if numero % 2 == 0:
        return False
    
    # verificamos si el número es divisible por algún número impar menor a su raíz cuadrada
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    
    # si la función no ha retornado False todavía, el número es primo
    return True
           