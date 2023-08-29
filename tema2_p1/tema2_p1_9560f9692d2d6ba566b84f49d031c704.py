from math import ceil, sqrt

def es_primo(n):
    if n == 1:
        return False
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True