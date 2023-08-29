def es_primo(numero):
    """
    Función que determina si un número es primo.
    Retorna True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero/2) + 1):
        if (numero % i) == 0:
            return False
    return True
