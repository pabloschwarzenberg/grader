# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    
    # Verificar si el número es divisible por algún número entre 2 y su raíz cuadrada
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    
    return True

# Ejemplos de uso
print(es_primo(7))  # True
print(es_primo(12))  # False
print(es_primo(23))  # True
