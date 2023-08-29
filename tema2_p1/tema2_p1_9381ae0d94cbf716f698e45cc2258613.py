# por favor escribe aquí tu función
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es un numero primo", n, "es un numero divisor")
            return False
    print("Es un numero primo")
    return True