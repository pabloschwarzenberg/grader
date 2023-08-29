#Cálculo del dígito verificador de un rut
import sys
import operator
import math

rut = input("Rut (primeros 8 digitos sin puntos): ")
rut_list = []
multiplicador = [3, 2, 7, 6, 5, 4, 3, 2]

if len(rut) == 7:
    rut_list.insert(0, "0")

for i in rut:
    rut_list.append(i)

rut_list_int = [int(x) for x in rut_list]

calculo = list(map(operator.mul, rut_list_int, multiplicador))


def dv(n):
    x = sum(list(n))
    e = math.floor(x / 11)
    f = x - (11 * e)
    h = 11 - f

    if (h == 11):
        h = "0"
    elif (h == 10):
        h = "k"
    return (h)


print("dv=",dv(calculo))