#Cálculo del dígito verificador de un rut

from itertools import cycle
rut= input("ingresa rut sin digito verificador:")
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
z=digito_verificador(rut)
if z == 10:
  z = 'k'
print("dv=",z)
  