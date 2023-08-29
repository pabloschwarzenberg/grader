# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


           