def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

           