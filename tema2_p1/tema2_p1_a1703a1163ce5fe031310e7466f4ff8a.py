# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False

    # Verificar divisibilidad por números menores
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

           