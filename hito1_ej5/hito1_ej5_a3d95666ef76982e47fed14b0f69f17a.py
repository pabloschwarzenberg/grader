#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]
    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

rut = input("Ingrese un número que represente un RUT (sin dígito verificador): ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)      