# por favor escribe aquí tu funcióndef es_primo(numero):
    def es_primo(numero):
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número menor a él
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

