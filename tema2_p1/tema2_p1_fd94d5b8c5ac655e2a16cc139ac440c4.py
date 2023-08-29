def es_primo(numero):
    """
    Función para determinar si un número es primo.

    Argumento:
    - numero: número entero positivo mayor que 1

    Retorna:
    - True si el número es primo, False si no lo es
    """
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True
