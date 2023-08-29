#Cálculo del dígito verificador de un rut
import sys
import operator
import math

rut = input("Ingrese el Rut sin puntos: ")
rut_ = []
num_cal = [3,2,7,6,5,4,3,2]

for i in rut:
  rut_.append(i)

rut_int = [int(x) for x in rut_]

calculo = list(map(operator.mul, rut_int, num_cal))

def dv(n):
    x = sum(list(n))
    e = math.floor(x / 11)
    f = x - (11 * e)
    h = 11 - f
    
    if (h == 11):
        h = "0"
    elif (h == 10):
        h = "k"
    return(h)

print("El digito verificador es:",dv(calculo))      