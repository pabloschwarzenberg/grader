""" Funciones y condicionales while: imprimir_factores_primos.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura while en Python
"""
def imprimir_factores_primos(numero):
    factor = 2
    while factor <= numero:
    # Verificar si el factor es un divisor de número
        if not (numero % factor != 0):
        # Si es así, imprímalo y divida el número original
            print(factor)
            numero /= factor
        else:
        # Si no es así, incremente el factor en uno
            factor += 1
    return "Done"
imprimir_factores_primos(100)      