def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:  # Si el número es divisible por algún divisor, no es primo
            return False
    
    return True

# Ejemplos de uso de la función
print(es_primo(7))   # True
print(es_primo(15))  # False
print(es_primo(29))  # True
           