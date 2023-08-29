#ejercicio hito 1 parte 4 primos
def es_primo(num):
    if num <=1:
        return False
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False    
    print("Es primo")
    return True   