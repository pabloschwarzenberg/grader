#Factores Primos

def imprimir_factores_primos(numero):
    
    factor = input()
    while factor <= numero:
        if not (numero % factor != 0):
            print(factor)
            numero /= factor
        else:
            factor += 1
    return "Done"
imprimir_factores_primos(factor)
 