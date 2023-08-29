#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reverso = rut_str[::-1]  # Invertir el orden del RUT
    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)


rut = input("Ingrese el RUT (sin puntos ni guión): ")
digito_verificador = calcular_digito_verificador(rut)
rut_completo = rut + '-' + digito_verificador

print("dv=" + digito_verificador)
