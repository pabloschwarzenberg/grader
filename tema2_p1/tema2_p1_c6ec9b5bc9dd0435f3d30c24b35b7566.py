# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, numero//2, 2):
        if numero % i == 0:
            return False
    return True