def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Si el número es divisible por otro número, no es primo
            return False
    
    return True  # Si el número no es divisible por ningún otro número, es primo
