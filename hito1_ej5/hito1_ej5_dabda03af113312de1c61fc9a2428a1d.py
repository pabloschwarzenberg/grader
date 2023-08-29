def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]
    factors = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5]
    sum = 0
    for i in range(len(reversed_rut)):
        sum += int(reversed_rut[i]) * factors[i]
    remainder = sum % 11
    dv = 11 - remainder
    if dv == 10:
        return "k"
    elif dv == 11:
        return "0"
    else:
        return str(dv)

# Solicitar al usuario que ingrese el RUT
rut = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)

      