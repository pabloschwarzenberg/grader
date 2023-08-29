#Cálculo del dígito verificador de un rut
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))    
    return (-s) % 11 
    
nrut=int(input("Ingrese RUT: "))
digito_verificador(nrut)
print("DV=" + str(digito_verificador(nrut)))
if digito_verificador(nrut)==10:
	resultado="k"
else:
	resultado=digito_verificador(nrut)
print("DV=" + str(resultado))