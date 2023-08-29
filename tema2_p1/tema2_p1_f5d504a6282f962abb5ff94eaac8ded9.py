# por favor escribe aquí tu función
def es_primo(numero):
    # Verificar si el número es menor o igual a 1
    if numero <= 1:
        return False

    # Verificar si el número es divisible por algún número diferente de 1 y sí mismo
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# Ejemplos de uso
print(es_primo(7))  # True
print(es_primo(10))  # False
print(es_primo(23))  # True
print(es_primo(1))  # False