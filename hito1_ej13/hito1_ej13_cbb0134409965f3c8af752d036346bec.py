import math
def imprimir_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if not ( numero % factor != 0):
            print(factor)
            numero /= factor
        else:
            factor += 1
    return "numero"
imprimir_factores_primos(100)     
if __name__=="__main__":
numero = imprimir_factores_primos("22")
print(numero)