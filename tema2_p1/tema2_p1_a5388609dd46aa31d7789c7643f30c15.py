def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

# Ejemplos de uso
print(es_primo(2))   # True
print(es_primo(7))   # True
print(es_primo(12))  # False
print(es_primo(23))  # True
print(es_primo(35))  # False

           