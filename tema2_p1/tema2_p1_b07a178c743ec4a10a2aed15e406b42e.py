

def es_primo(numero):
    if numero < 2:    # los números primos son mayores a 1
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True