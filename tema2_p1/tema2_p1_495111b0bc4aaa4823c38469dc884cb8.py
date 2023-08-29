# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    limite = int(round((numero)**(1/2)))

    i = 3
    while i <= limite:
        if numero % i == 0:
            return False
        i = i + 3

    return True