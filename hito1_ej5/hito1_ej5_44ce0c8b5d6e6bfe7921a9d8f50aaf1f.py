#Cálculo del dígito verificador de un rut
      
      
 rut=int(input("Ingrese un numero:"))


def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

print(digito_verificador(rut))
