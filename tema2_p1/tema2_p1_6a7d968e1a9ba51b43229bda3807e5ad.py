# por favor escribe aquí tu función
def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    if numero == 1 or numero == 0:
        return False
    return True
           