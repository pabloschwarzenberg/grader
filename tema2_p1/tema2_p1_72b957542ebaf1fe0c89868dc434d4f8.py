def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    # Si no es divisible por ningún número, es primo
    return True
           