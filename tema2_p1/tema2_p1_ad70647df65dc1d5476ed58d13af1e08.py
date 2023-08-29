# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:  # Si el número es divisible por otro número, no es primo
            return False
    return True