#libreria
from itertools import cycle

#Funcion
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    s = (-s) % 11
    if (s == 10) :
        s = 'k' 
    return s

#Rut
rut = input('Ingrese un rut');

#Digito verificador
dv = 0;
dv = digito_verificador(rut);

#Print
print('dv='+str(dv))