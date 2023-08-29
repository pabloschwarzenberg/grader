# por favor escribe aquí tu función
def es_primo(num):
# Los números menores que 2 no son primos
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
# Si el número es divisible por algún número entre 2 y su raíz cuadrada, no es primo    
    else:
        divisor = 5
        while divisor * divisor <= num:
            if num % divisor == 0 or num % (divisor + 2) == 0:
                return False
            divisor += 6
        return True
           