def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Si el número es divisible por otro número, no es primo
            return False

    return True  # Si no es divisible por ningún número, es primo

# Ejemplos de uso:
print(es_primo(7))  # True
print(es_primo(12))  # False
print(es_primo(29))  # True
