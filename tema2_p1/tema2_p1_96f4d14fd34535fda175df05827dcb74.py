# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplos de uso
print(es_primo(7))    # True
print(es_primo(16))   # False
print(es_primo(23))   # True

           