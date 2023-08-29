# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False

    # Verificar si el número es divisible por algún número desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True  # Si no se encontró ningún divisor, el número es primo


# Ejemplos de uso
print(es_primo(7))  # Salida: True
print(es_primo(10))  # Salida: False
print(es_primo(13))  # Salida: True
