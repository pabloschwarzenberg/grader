def es_primo(num):
    if num < 2:  # Los números menores a 2 no son primos
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True