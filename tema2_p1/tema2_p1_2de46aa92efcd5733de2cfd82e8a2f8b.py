def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    
    # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # El número es divisible, por lo tanto no es primo
    
    return True  # El número no es divisible por ningún otro número, es primo