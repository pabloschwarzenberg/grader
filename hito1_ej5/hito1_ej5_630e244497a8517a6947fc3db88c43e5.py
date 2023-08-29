#Cálculo del dígito verificador de un rut
# Pedir al usuario que ingrese el número del RUT sin el dígito verificador
def calcular_digito_verificador(rut):
    rut_invertido = str(rut)[::-1]
    factor = 2
    suma = 0
    for digito in rut_invertido:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)

numero_rut = input("Ingresa un número de RUT: ")
digito_verificador = calcular_digito_verificador(numero_rut)
print("dv =", digito_verificador)
