# por favor escribe aquí tu función
def es_primo(numero):
    for n in range(1, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True