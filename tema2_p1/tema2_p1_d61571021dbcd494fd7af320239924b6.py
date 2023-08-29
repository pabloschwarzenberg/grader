# por favor escribe aquí tu función
def es_primo(numero):
    y = False
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                y = True
                break
    else:
        return False
    if y:
        return False
    else:
        return True

es_primo(1)
