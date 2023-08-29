# por favor escribe aquí tu función
def es_primo(numero):
    if numero<2:
        return False
    for num in range(2,numero):
        if numero % num == 0:
            return False
        return True