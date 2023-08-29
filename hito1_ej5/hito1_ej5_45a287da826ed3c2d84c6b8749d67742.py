#Cálculo del dígito verificador de un rut
# codificación=utf-8

# Obtener el dígito verificador del RUT en Python.
#
# La función recibe el RUT como un entero,
# y entrega el dígito verificador como un entero.
# Si el resultado es 10, el RUT es "raya k".

desde el ciclo de importacion de itertools

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut))))
    factores = ciclo(rango(2, 8))
    s = suma(d * f para d, f en zip(reversed_digits, factores))
    retorno (-s) % 11      