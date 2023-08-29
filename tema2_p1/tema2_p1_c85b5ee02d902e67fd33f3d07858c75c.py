def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    
    # Comprobamos si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

# Ejemplos de uso
print(es_primo(7))  # True
print(es_primo(10))  # False
print(es_primo(29))  # True

           