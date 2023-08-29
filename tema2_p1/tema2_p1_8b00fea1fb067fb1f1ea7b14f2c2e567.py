def es_primo(numero):
    # Casos especiales
    if numero <= 1:
        return False
    if numero == 2:
        return True

    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True