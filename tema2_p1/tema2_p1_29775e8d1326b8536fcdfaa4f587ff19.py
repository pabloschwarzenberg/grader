def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False

    # Verificar si el número es divisible por algún número entre 2 y su mitad
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False

    return True

# Ejemplos de uso
print(es_primo(7))   # True
print(es_primo(10))  # False
print(es_primo(13))  # True
