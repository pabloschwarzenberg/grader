#calculo digito verificador
def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]
    factors = [2, 3, 4, 5, 6, 7, 2, 3]
    total = sum(int(digit) * factor for digit, factor in zip(reversed_rut, factors))
    remainder = total % 11
    dv = 11 - remainder if remainder != 0 else 0
    return dv

# Solicitar el RUT al usuario
rut_input = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut_input)

# Imprimir el resultado
print("dv =", digito_verificador)



    