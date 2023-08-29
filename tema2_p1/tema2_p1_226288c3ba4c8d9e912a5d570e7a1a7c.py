def es_primo(numero):
    # Los números negativos, 0 y 1 no son primos
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True