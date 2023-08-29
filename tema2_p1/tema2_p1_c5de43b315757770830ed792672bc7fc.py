# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False

    # Verificar si el número es divisible por algún número menor que él mismo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

           