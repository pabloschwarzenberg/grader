#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]
    factor = 2
    suma = 0
    for d in reversed_rut:
        suma += int(d) * factor
        factor = factor + 1 if factor < 7 else 2
    verificador = 11 - (suma % 11)
    if verificador == 11:
        return '0'
    elif verificador == 10:
        return 'K'
    else:
        return str(verificador)

rut = input("Ingrese un número de RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
