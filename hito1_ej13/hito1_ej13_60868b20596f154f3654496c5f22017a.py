#Factores Primos
n = int(input('ingresa un numero'))

def imprimir_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if not (numero % factor != 0):
            print(factor)
            numero /= factor
        else:
            factor += 1
    return "Done"      


imprimir_factores_primos(n)
      