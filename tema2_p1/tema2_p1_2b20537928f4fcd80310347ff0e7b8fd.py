from math import sqrt

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True
