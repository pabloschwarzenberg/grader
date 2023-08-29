# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:  
        print(numero, "no es primo")
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            print(numero, "no es primo")
            return False
    print(numero, "es primo")
    return True
           