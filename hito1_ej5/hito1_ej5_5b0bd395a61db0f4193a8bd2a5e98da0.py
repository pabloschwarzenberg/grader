#Cálculo del dígito verificador de un rut
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if(-s)%11==10:
      return str("k")
    else:
     return (-s) % 11
  
run=int(input("ingrega rut"))
print("dv=",digito_verificador(run))