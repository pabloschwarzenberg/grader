def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

# Ejemplo de uso
print(es_primo(17))  # True
print(es_primo(10))  # False
