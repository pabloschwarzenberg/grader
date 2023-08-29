# por favor escribe aquí tu función
def es_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False


