# por favor escribe aquí tu función
def es_primo(z):
    if z < 2:
        return False

    for num in range(2,z):
        if z%num == 0:
            return False

    return True             