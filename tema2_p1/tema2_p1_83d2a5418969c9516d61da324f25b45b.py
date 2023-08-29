# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return False
            else:
                return True