#por favor escribe aquí tu función
def es_primo(numero):
    # Casos especiales para 0, 1 y números negativos
    if numero < 2:
        return False

    # Verificar si el número es divisible por algún número menor a su raíz cuadrada
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True
