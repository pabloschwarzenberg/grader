#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1] 
    multiplicador = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = "k"
    elif digito_verificador == 10:
        digito_verificador = "k"

    return digito_verificador


rut = int(input("Ingrese el RUT sin el dígito verificador: "))
digito_verificador = calcular_digito_verificador(rut)
print("dv=",digito_verificador)
    