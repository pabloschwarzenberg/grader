#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    factor = 2
    suma = 0

    for i in range(len(rut_str) - 1, -1, -1):
        suma += int(rut_str[i]) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador


rut = input("Ingrese el número de rut (sin dígito verificador): ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)