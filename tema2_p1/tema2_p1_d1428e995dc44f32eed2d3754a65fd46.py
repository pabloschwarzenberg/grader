import math

def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True