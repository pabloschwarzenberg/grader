#Cálculo del dígito verificador de un rut
from itertools import cycle
rut = eval(input("ingrese el rut sin guion: "))

def digitov(rut):
    digitosresv = map(int, reversed(str(rut)))
    factores = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(digitosresv, factores))
    return (-s) % 11

if digitov(rut)==10:
        print("dv=k")
else:
    print("dv=",digitov(rut))     