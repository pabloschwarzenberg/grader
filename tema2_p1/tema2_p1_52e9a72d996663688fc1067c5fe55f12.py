# por favor escribe aquí tu función
def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número entre 2 y su mitad (inclusive)
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False

    # Si el número no es divisible por ningún otro número, es primo
    return True