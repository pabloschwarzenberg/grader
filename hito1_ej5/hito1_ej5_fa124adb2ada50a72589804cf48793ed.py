#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reversed = rut[::-1]
    factor = 2
    suma = 0

    for d in rut_reversed:
        suma += int(d) * factor
        factor += 1
        if factor == 8:
            factor = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

rut = int(input("Ingrese el número de Rut (sin dígito verificador): "))

digito_verificador = calcular_digito_verificador(rut)
print("dv=" + str(digito_verificador))