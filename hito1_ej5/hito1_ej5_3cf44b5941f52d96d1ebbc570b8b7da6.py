def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

# Entrada de datos
rut = input("Ingrese el número de RUT sin dígito verificador: ")

# Calcula el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprime el resultado
print("dv =", dv)