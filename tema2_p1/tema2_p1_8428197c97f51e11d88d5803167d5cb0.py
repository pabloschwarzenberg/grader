# por favor escribe aquí tu función
 def es_primo(numero):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Comprobamos si es divisible por algún número impar
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True       