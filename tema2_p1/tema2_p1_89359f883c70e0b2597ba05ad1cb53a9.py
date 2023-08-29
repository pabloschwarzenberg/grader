def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:  # Si el número es divisible por algún divisor, no es primo
            return False
    return True


# Ejemplos de uso de la función es_primo
print(es_primo(2))   # True
print(es_primo(3))   # True
print(es_primo(10))  # False
print(es_primo(13))  # True
           