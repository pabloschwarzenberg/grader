# por favor escribe aquí tu función
def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    # Si no se encontró ningún divisor, el número es primo
    return True