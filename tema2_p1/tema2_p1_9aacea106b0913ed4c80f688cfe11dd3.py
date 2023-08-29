# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

# Ejemplos de uso
print(es_primo(7))   # Devuelve True
print(es_primo(12))  # Devuelve False
print(es_primo(31))  # Devuelve True